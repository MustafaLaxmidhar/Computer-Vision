import cv2
import numpy as np
import os
import ColourProcessing 
import ImageCrop
import Threshold
import CountPixels
import EdgeDetection
from matplotlib import pyplot as plt

def process_image(parentfolder, subfolder, image_name):
    # Define the path to the image
    src = os.path.join(parentfolder, subfolder, image_name)

    # Opens image in grayscale
    image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

    # Crop image
    x_origin = 0
    y_origin = 0
    x_width = len(image[1,:])
    y_width = 150
    cropped_image = ImageCrop.crop_image(image, x_origin, y_origin, x_width, y_width)
    #cv2.imshow("cropped image", cropped_image)

    # Increase contrast of image
    contrasted_image = ColourProcessing.increase_contrast(cropped_image)
    #cv2.imshow("contrasted image", contrasted_image)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(contrasted_image, (5, 7), 0)

    # Find edges
    _, thresholded_image = cv2.threshold(blurred_image, 120, 255, cv2.THRESH_BINARY)
    edges = EdgeDetection.find_edges(thresholded_image)
    pixel = CountPixels.count_pixels(edges)
    #cv2.imshow("edged image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

