import argparse

from photo_sorter import ResultsAggregator


def main(input_dir: str,
         output_dir: str,
         n_jobs: int,
         detect_rotated_images: bool,
         skip_original_angle_images: bool):
    """
    currently main only set to copy photos without faces to output_dir!
    :param skip_original_angle_images:
    :param detect_rotated_images: run detection for rotated images or not (takes longer!)
    :param input_dir: input directory
    :param output_dir: output directory
    :param n_jobs: jobs to run in parallel
    :return:
    """
    results_agg = ResultsAggregator(input_dir,
                                    n_jobs=n_jobs,
                                    detect_rotated=detect_rotated_images,
                                    skip_original_angle=skip_original_angle_images)
    results_agg.run_detection()
    if output_dir:
        results_agg.copy_photos_to_output_dir(output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='get command line options')
    parser.add_argument("-i", "--input_dir", type=str,
                        help='input dir to read and detect faces')
    parser.add_argument("-o", "--output_dir", type=str, default="",
                        help='output dir to copy files without faces to')
    parser.add_argument("-n", "--n_jobs", type=int, default=4,
                        help='number of jobs to run in parallel')
    parser.add_argument("-r", "--rotate", type=bool, default=False,
                        help='whether to detect images when rotated 90, 180, 270 as well')
    parser.add_argument("-s", "--skip", type=bool, default=False,
                        help='whether to skip original image for facial recognition (only do rotated?)')
    args = parser.parse_args()
    my_input_path = args.input_dir
    my_output_path = args.output_dir
    my_n_jobs = args.n_jobs
    detect_rotated = args.rotate
    skip_original = args.skip
    main(my_input_path, my_output_path, my_n_jobs,
         detect_rotated_images=detect_rotated,
         skip_original_angle_images=skip_original
         )
