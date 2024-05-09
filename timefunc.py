import Filter2
import CountPixels
import time
import cv2
import numpy as np
import os
import MusMethod
from matplotlib import pyplot as plt

# Define the parameters for processing the image
parentfolder = "WeldGapImages"
subfolder = "Set 3"
image_name = "image0300.jpg"  # or whatever the image file name is
    
src = os.path.join(parentfolder, subfolder, image_name)


# Call the process_image function from the image_processing module
start_time = time.time()
# Filter2.process_image(parentfolder, subfolder, image_name)
image = MusMethod.image_processing(src)
weldgap_positions = CountPixels.count_pixels(image)
weldgap_drawing = CountPixels.draw_highest_pixel(src, weldgap_positions)
end_time = time.time()

cv2.imshow("DEEZ NUTS" , weldgap_drawing)
cv2.waitKey(0)
                                
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
