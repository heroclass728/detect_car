import cv2
import os
import ntpath

from utils.constants import CUR_DIR, IMAGE_MAX_HEIGHT, IMAGE_MAX_WIDTH


class ImageResize:

    def __init__(self):

        self.output_dir = os.path.join(CUR_DIR, 'output')

    def resize_image(self, image_path):

        file_path = ntpath.basename(image_path)
        head, tail = ntpath.split(file_path)
        origin_file_name = tail.replace(".jpg", "")
        resized_file_name = origin_file_name + "_resized" + ".jpg"
        output_file_path = os.path.join(self.output_dir, resized_file_name)

        car_image = cv2.imread(image_path)
        car_image_width = car_image.shape[1]
        car_image_height = car_image.shape[0]

        if car_image_width > IMAGE_MAX_WIDTH or car_image_height > IMAGE_MAX_HEIGHT:

            resize_ratio = 1
            if car_image_width > IMAGE_MAX_WIDTH:

                resize_ratio = IMAGE_MAX_WIDTH / car_image_width
            elif car_image_height > IMAGE_MAX_HEIGHT:

                resize_ratio = IMAGE_MAX_HEIGHT / car_image_height

            resized_image = cv2.resize(car_image, None, fx=resize_ratio, fy=resize_ratio, interpolation=cv2.INTER_CUBIC)
        else:

            resized_image = car_image

        cv2.imwrite(output_file_path, resized_image)

        return resized_image, origin_file_name
