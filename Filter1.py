import cv2
import numpy as np
import os

#pathfile for image 
# Define the path to the image and the subfolder
subfolder = "Set1"
image_name = "image0001.jpg"  # or whatever the image file name is
src = os.path.join(subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

# Gassuian blur to reuce noise in image
# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (7, 7), 0)

high_thresh = 90
maxval = 255

# use highpass filter to isolate line
retval, blurred_highpass = cv2.threshold(blurred, high_thresh, maxval, cv2.THRESH_BINARY)
retval, withoutblur_highpass =  cv2.threshold(image, high_thresh, maxval, cv2.THRESH_BINARY)
#display all images
cv2.imshow("without gaussian blur", blurred_highpass)
cv2.imshow("with gaussian blur", withoutblur_highpass)
cv2.waitKey(0)
