import os
import glob

from utils.constants import CUR_DIR
from image_processing.image_resize import ImageResize
from car_detection.sub_detection import SubDetection
from image_processing.xml_creation import XMLCreation


class MainDetection:

    def __init__(self):

        self.input_dir = os.path.join(CUR_DIR, 'input')
        self.ouput_dir = os.path.join(CUR_DIR, 'output')
        self.image_resize = ImageResize()
        self.sub_detection = SubDetection()
        self.xml_creation = XMLCreation()

    def main_detect(self):

        for root, car_image_dirs, files in os.walk(self.input_dir):

            for dir_name in car_image_dirs:

                car_image_paths = glob.glob(os.path.join(root, dir_name, "*.jpg"))
                output_dir_path = os.path.join(self.ouput_dir, dir_name)
                if car_image_paths is not None and os.path.exists(output_dir_path) is False:

                    os.mkdir(output_dir_path)

                for car_image_path in car_image_paths:

                    car_image, org_filename, file_path, file_width, file_height\
                        = self.image_resize.resize_image(car_image_path, dir_name)
                    prominent_car = self.sub_detection.detect_cars_image(car_image, org_filename, dir_name)
                    self.xml_creation.create_xml(prominent_car, dir_name, org_filename, file_path, file_width,
                                                 file_height)
