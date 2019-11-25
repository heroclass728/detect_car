import os
import xml.etree.ElementTree as ET
import ntpath

from utils.constants import CUR_DIR
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom


class XMLCreation:

    def __init__(self):

        self.output_dir = os.path.join(CUR_DIR, 'output')

    def create_xml(self, coordinates, dirname, file_name, file_path, file_width, file_height):

        xml_file_name = file_name + "_resized" + ".xml"
        output_xml_file_path = os.path.join(self.output_dir, dirname, xml_file_name)
        base_file_path = ntpath.basename(file_path)
        folder_path = os.path.dirname(file_path)

        # Configure one attribute with set()
        root = Element('annotation')

        folder = SubElement(root, 'folder')
        folder.text = folder_path
        filename = SubElement(root, 'filename')
        filename.text = base_file_path
        path = SubElement(root, 'path')
        path.text = file_path

        source = SubElement(root, 'source')
        database = SubElement(source, 'database')
        database.text = "Unknown"

        size = SubElement(root, 'size')
        width = SubElement(size, 'width')
        width.text = str(file_width)
        height = SubElement(size, 'height')
        height.text = str(file_height)
        depth = SubElement(size, 'depth')
        depth.text = "3"

        segmented = SubElement(root, 'segmented')
        segmented.text = "0"

        object_element = SubElement(root, 'object')

        name = SubElement(object_element, 'name')
        name.text = dirname
        pose = SubElement(object_element, 'pose')
        pose.text = "Unspecified"
        truncated = SubElement(object_element, 'truncated')
        truncated.text = "0"
        difficult = SubElement(object_element, 'difficult')
        difficult.text = "0"

        bnd_box = SubElement(object_element, 'bndbox')
        x_min = SubElement(bnd_box, 'xmin')
        x_min.text = str(int(coordinates[0]))
        y_min = SubElement(bnd_box, 'ymin')
        y_min.text = str(int(coordinates[1]))
        x_max = SubElement(bnd_box, 'xmax')
        x_max.text = str(int(coordinates[2]))
        y_max = SubElement(bnd_box, 'ymax')
        y_max.text = str(int(coordinates[3]))

        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

        f = open(output_xml_file_path, "w")
        f.write(xml_str)

        print("Successfully created {}".format(xml_file_name))
