import shutil
import unittest
import os
from photo_sorter import ResultsAggregator

test_data_dir = os.path.dirname(os.path.realpath(__file__))


class TestFacialDetectorFreshRun(unittest.TestCase):
    def setUp(self):
        self.expected_results = {
            "IMG_5018.JPG": 0,
            "IMG_5019.JPG": 0,
            "EdSheeran.jpg": 1,
            "JenniferAniston.jpg": 1,
            "KatharineMcPhee.jpg": 1,
            "NickZanoElishaCuthbertKellyBrook.jpg": 3
        }
        self.test_input_dir = os.path.join(test_data_dir, "../common")
        self.test_no_face_output_dir = os.path.join(test_data_dir, "../dummy/test_output_no_face/")
        self.test_has_face_output_dir = os.path.join(test_data_dir, "../dummy/test_output_has_face/")

    def test_run_entire_facial_detector_pipeline(self):
        results_agg = ResultsAggregator(self.test_input_dir, n_jobs=5)
        results_agg.run_detection()
        results_agg.copy_photos_to_output_dir(has_face=False,
                                              output_dir=self.test_no_face_output_dir)
        results_agg.copy_photos_to_output_dir(has_face=True,
                                              output_dir=self.test_has_face_output_dir)

        self.assertTrue(os.path.isfile("facial_detection_record.csv"))
        self.assertTrue(os.path.isfile(
            os.path.join(self.test_no_face_output_dir, "common/IMG_5019.JPG")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.test_has_face_output_dir, "common/EdSheeran.jpg")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.test_has_face_output_dir, "common/JenniferAniston.jpg")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.test_has_face_output_dir, "common/KatharineMcPhee.jpg")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.test_has_face_output_dir, "common/NickZanoElishaCuthbertKellyBrook.jpg")))

    def tearDown(self):
        os.remove("facial_detection_record.csv")
        shutil.rmtree(self.test_no_face_output_dir)
        shutil.rmtree(self.test_has_face_output_dir)
