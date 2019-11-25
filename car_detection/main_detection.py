import os
import glob

from utils.constants import CUR_DIR
from image_processing.image_resize import ImageResize
from car_detection.sub_detection import SubDetection
from image_processing.xml_creation import XMLCreation


class MainDetection:

    def __init__(self):

        self.input_dir = os.path.join(CUR_DIR, 'input')
        self.image_resize = ImageResize()
        self.sub_detection = SubDetection()
        self.xml_creation = XMLCreation()

    def main_detect(self):

        car_image_paths = glob.glob(os.path.join(self.input_dir, "*.jpg"))

        for car_image_path in car_image_paths:

            car_image, filename = self.image_resize.resize_image(car_image_path)
            prominent_car = self.sub_detection.detect_cars_image(car_image, filename)
            # self.xml_creation.create_xml(prominent_car)
