# DetectCar

## Overview

This project is to detect all the cars in the image, choose the main one of them and save it's information(position) 
into xml file.

## Project Structure

- car detection

    The main source to detect the cars and select the main car in the image.

- image_processing

   The source to resize the image and create xml files with the car information

- input

    The images according to car type are contained.

- output
    
    According to the car type, the images with the detected car and xml files with it's information

- utils

    constants with several settings and models to detect car(.pb, .pbtxt, .config).
    The frcnn_inception_v2 model is used in this project.

- main

    The main execution file
    
- requirements.txt

    The several libraries for this project

## Project Installation

- Environment

    Ubuntu 18.04, Python 3.6

- Library Installation
    
    ```
        pip3 install -r requirements.txt
    ```

- Download frnn_inception_v2 model(.pb, .pbtxt) from the model zoo, make config file from them and copy all of the three files in 
uitls directory. 

## Project Execution

- Please copy the car images to detect in input directory according to car type or if you don't know car type, all the 
images in input directory.

- Please run the following command in terminal

    ```
        python3 main.py
    ```
