import cv2
import numpy as np
import os

from utils.constants import CUR_DIR


class SubDetection:

    def __init__(self):

        self.model_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2.pb')
        self.graph_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2_graph.pbtxt')
        self.labelimg_output_dir = os.path.join(CUR_DIR, 'output')

    def detect_cars_image(self, frame, filename):

        label_file_name = filename + "_LabelIMg" + ".jpg"
        label_output_file_path = os.path.join(self.labelimg_output_dir, label_file_name)

        cvNet = cv2.dnn.readNetFromTensorflow(self.model_path, self.graph_path)

        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        print(frame_width, frame_height)
        cvNet.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        detected_car_boundaries = []
        area_boundary = []
        for detection in cvOut[0, 0, :, :]:
            score = float(detection[2])
            label = int(detection[1])
            if score > 0.3 and label == 2:
                left = detection[3] * frame_width
                top = detection[4] * frame_height
                right = detection[5] * frame_width
                bottom = detection[6] * frame_height

                area = (right - left) * (bottom - top)

                detected_car_boundaries.append((left, top, right, bottom))
                area_boundary.append(area)
                cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

        max_index = int(np.argmax(area_boundary))
        max_boundary = detected_car_boundaries[max_index]
        cv2.rectangle(frame, (int(max_boundary[0]), int(max_boundary[1])),
                      (int(max_boundary[2]), int(max_boundary[3])), (0, 0, 255), thickness=3)
        cv2.imwrite(label_output_file_path, frame)

        return max_boundary
        # cv2.imshow('img', frame)
        # cv2.waitKey()
