import os
import shutil
import logging
import csv

from joblib import Parallel, delayed

from photo_sorter.facial_detector import FacialDetector

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ResultsAggregator:
    def __init__(self,
                 dir_to_process: str,
                 detection_record_csv: str = "facial_detection_record.csv",
                 batch_size: int = 500,
                 formats_allowed: tuple = None,
                 n_jobs: int = 8,
                 detect_rotated=False,
                 skip_original_angle=False
                 ):
        """
        1. loads detection record (csv file with columns "filepath" and "has_faces"
        2. reads directory of interest, gets list of photos not in detection record
        3. runs (in batches set by batch_size) facial detector on photos
        4. appends records to detection record csv (writes this per batch)
        If run fails, this can be picked up as the csv will be updated per batch of run

        Another mode to run this script (after the above) can be used to load detention_record_csv,
        copy photos without (or with) faces to specified directory (for uploading online)

        :param dir_to_process: os walks to get relevant photos to be read
        :param detection_record_csv:
        :param batch_size: batch size per run; will write to detection_record after each batch run
        :param formats_allowed:
        :param n_jobs:
        """
        logger.info("Initializing ResultsAggregator")
        self.dir_to_process = dir_to_process
        self.detection_record_csv = detection_record_csv
        self.batch_size = batch_size
        self.formats_allowed = (".jpg", ".jpeg", ".png") if formats_allowed is None else formats_allowed
        self.n_jobs = n_jobs

        self.saved_records = dict()
        self.files_to_process = []

        self.detection_results = None
        self.file_results_list = None
        self.detect_rotated = detect_rotated
        self.skip_original_angle = skip_original_angle

    def _update_saved_records(self):
        if os.path.isfile(self.detection_record_csv):
            with open(self.detection_record_csv, newline='') as csvfile:
                self.saved_records = {x[0]: x[1] for x in csv.reader(csvfile)}

    def _load_files_to_analyse(self):
        # TODO can be sped up with less for loops?
        for root, _dirs, files in os.walk(self.dir_to_process):
            for file in files:
                filepath = os.path.join(root, file)
                if file.lower().endswith(self.formats_allowed) and filepath not in self.saved_records:
                    self.files_to_process.append(filepath)
        logger.info("files to analyse: " + str(len(self.files_to_process)))

    def _run_detection_for_single_file(self, file):
        try:
            logging.info("Processed file: " + str(file))
            detector = FacialDetector(
                detect_rotated=self.detect_rotated,
                skip_original_angle=self.skip_original_angle)
            detector.detect_faces(file)
            return len(detector.face_locations)
        except Exception as e:
            logging.info(e)
            return False

    def run_detection(self):
        self._update_saved_records()
        self._load_files_to_analyse()

        if len(self.files_to_process) == 0:
            logger.info("no new files need to be processed...")
        else:
            total_number_of_runs = len(self.files_to_process) // self.batch_size + 1

            for x in range(total_number_of_runs):
                logger.info(f"Processing batch {x} of {total_number_of_runs}")
                subset_to_be_analysed = self.files_to_process[self.batch_size * x: self.batch_size * (x + 1)]
                detection_results = Parallel(n_jobs=self.n_jobs)(delayed(self._run_detection_for_single_file)(file)
                                                                 for file in subset_to_be_analysed)
                file_results_list = list(zip(subset_to_be_analysed, detection_results))
                self._write_results_to_file(file_results_list)
            logger.info("Done with face detection...")

    def _write_results_to_file(self, file_results_list):
        logger.info("Writing results to file")
        with open(self.detection_record_csv, "a") as f:
            csv_writer = csv.writer(f)
            [csv_writer.writerow(x) for x in file_results_list]

    def copy_photos_to_output_dir(self,
                                  output_dir,
                                  has_face: bool = False
                                  ):
        self._update_saved_records()
        if has_face:
            filepaths_to_copy = [x for x in self.saved_records if int(self.saved_records[x]) > 0]
        else:
            filepaths_to_copy = [x for x in self.saved_records if int(self.saved_records[x]) == 0]

        for to_copy in filepaths_to_copy:
            output_filepath = os.path.join(output_dir, "/".join(to_copy.split("/")[-2:]))
            logger.info("Copying files to " + str(output_filepath))
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
            shutil.copy2(to_copy, output_filepath)
