import Filter2
import CountPixels
import time
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Define the parameters for processing the image
parentfolder = "WeldGapImages"
subfolder = "Set 3"
image_name = "image0300.jpg"  # or whatever the image file name is
    
src = os.path.join(parentfolder, subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
# Call the process_image function from the image_processing module
start_time = time.time()
# Filter2.process_image(parentfolder, subfolder, image_name)
CountPixels.white_pixel_counts(image)
end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
