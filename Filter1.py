import cv2
import numpy as np
import os
import ColourProcessing 
import ImageCrop
import Threshold
import CountPixels
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

EdgeDetection.apply_dft_and_display_heatmap(image)


# crop image
x_origin = 0
y_origin = 0
x_width = len(image[1,:])
y_width = 150
cropped_image = ImageCrop.crop_image(image, x_origin, y_origin, x_width, y_width)
cv2.imshow("cropped image", cropped_image)

#increase Contrast of image
contrasted_image = ColourProcessing.increase_contrast(cropped_image)
cv2.imshow("contrasted image", contrasted_image)


# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(contrasted_image, (5, 7), 0)
_, thresholded_image = cv2.threshold(blurred_image, 120, 255, cv2.THRESH_BINARY)
cv2.circle(thresholded_image, (993, 70), 1, (0, 255, 0), -1)
cv2.imshow("blurred image", blurred_image)
cv2.imshow("thresholded image", thresholded_image)

# add_dark_image = ColourProcessing.add_dark(blurred_image)
# removed_light_image = ColourProcessing.remove_light(add_dark_image)

edges = EdgeDetection.find_edges(thresholded_image)

pixel = CountPixels.count_pixels(edges)
cv2.imshow("edged image", pixel)

cv2.circle(cropped_image, (993, 70), 1, (0, 255, 0), -1)
cv2.imshow("green dot image", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

