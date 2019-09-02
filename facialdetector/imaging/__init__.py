import cv2
import matplotlib.pyplot as plt
import face_recognition
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class FacialDetector:
    """
    Classifier that runs through images and detects whether they have faces in each photo.
    Stores each photo filepath as a dictionary key, with the number of faces stored as values
    Has option to output move image
    """

    def __init__(self):
        self.loaded_img = None
        self.rgb_img = None
        self.face_locations = None

    def detect_faces(self,
                     input_filepath: str):
        self.loaded_img = cv2.imread(input_filepath)
        self.rgb_img = self.loaded_img[:, :, ::-1]
        self.face_locations = face_recognition.face_locations(self.rgb_img)

    def visualiser(self,
                   show_visualiser: bool = True,
                   output_filepath: str = ""):
        for (top, right, bottom, left) in self.face_locations:
            cv2.rectangle(self.loaded_img,
                          (left, top),
                          (right, bottom),
                          (0, 255, 0),
                          20)
        plt.imshow(self.rgb_img)
        if output_filepath:
            plt.savefig(output_filepath[:-3] + "png")
        if show_visualiser:
            plt.show()
