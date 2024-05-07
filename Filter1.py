import cv2
import numpy as np
import os
import ColourProcessing 
import ImageCrop
import Threshold
import EdgeDetection
from matplotlib import pyplot as plt

#pathfile for image 
# Define the path to the image and the subfolder
parentfolder = "WeldGapImages"
subfolder = "Set 3"
image_name = "image0300.jpg"  # or whatever the image file name is
src = os.path.join(parentfolder, subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

# crop image
x_origin = 0
y_origin = 0
x_width = len(image[1,:])
y_width = 400
cropped_image = ImageCrop.crop_image(image, x_origin, y_origin, x_width, y_width)
cv2.imshow("cropped image", cropped_image)

#increase Contrast of image
contrasted_image = ColourProcessing.increase_contrast(cropped_image)
cv2.imshow("contrasted image", contrasted_image)


# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(contrasted_image, (5, 7), 0)

edges = EdgeDetection.find_edges(blurred_image)
cv2.imshow("edged image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

