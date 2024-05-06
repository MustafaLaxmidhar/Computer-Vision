import cv2
import numpy as np
import os
import FindColor 
import ImageCrop
import Threshold

#pathfile for image 
# Define the path to the image and the subfolder
parentfolder = "WeldGapImages"
subfolder = "Set 1"
image_name = "image0001.jpg"  # or whatever the image file name is
src = os.path.join(parentfolder, subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

# crop image
x_origin = 800
y_origin = 0
x_width = 300
y_width = 400
cropped_image = ImageCrop.crop_image(image, x_origin, y_origin, x_width, y_width)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(cropped_image, (7, 7), 0)

maxval = 255
# Finding most abundant colour in image as startpoint for thresholding
thresh = FindColor.most_abundant_colour(blurred_image)
print(thresh)
retval, start = cv2.threshold(blurred_image, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold start", start)
cv2.waitKey(0)
cv2.destroyAllWindows()


#increases threshold until number of black pixels is reached
weldgap_area = 4341             #obtained by width of weld gap x height of cropped image
threshold = Threshold.find_threshold(blurred_image, 3300, thresh)


# use highpass filter to isolate line
retval, output = cv2.threshold(blurred_image, threshold, maxval, cv2.THRESH_BINARY)
cv2.imshow("threshold test", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

