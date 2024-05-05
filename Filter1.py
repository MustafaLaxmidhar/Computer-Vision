import cv2
import numpy as np
import os
import FindColor 

#pathfile for image 
# Define the path to the image and the subfolder
subfolder = "Set2"
image_name = "image0200.jpg"  # or whatever the image file name is
src = os.path.join(subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)



# Gassuian blur to reuce noise in image
# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (7, 7), 0)

high_thresh = FindColor.most_abundant_colour(image)
high_thresh = high_thresh - 130
maxval = 255

# use highpass filter to isolate line
retval, blurred_highpass = cv2.threshold(blurred, high_thresh, maxval, cv2.THRESH_BINARY)
retval, withoutblur_highpass =  cv2.threshold(image, high_thresh, maxval, cv2.THRESH_BINARY)
#display all images
cv2.imshow("without gaussian blur", blurred_highpass)
cv2.imshow("with gaussian blur", withoutblur_highpass)
cv2.waitKey(0)
