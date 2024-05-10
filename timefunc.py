import Filter2
import CountPixels
import time
import cv2
import numpy as np
import os
import MusMethod
from matplotlib import pyplot as plt

# Define the parameters for processing the image
#parentfolder = "WeldGapImages"
#subfolder = "Set 3"
#image_name = "image0300.jpg"  # or whatever the image file name is
def process_image(parentfolder, subfolder, image_name):   
    src = os.path.join(parentfolder, subfolder, image_name)


    # Call the process_image function from the image_processing module
    start_time = time.time()
    # Filter2.process_image(parentfolder, subfolder, image_name)
    image = MusMethod.image_processing(src)
    weldgap_positions = CountPixels.find_consecutive_black_pixels(image, 5)
    weldgap_drawing = CountPixels.draw_shapes(src, weldgap_positions)
    weldgap = CountPixels.find_most_coordinates_range(weldgap_positions, weldgap_drawing.shape[1], 10)
    weldgap_drawing = CountPixels.draw_shapes(src, weldgap)
    gradient, intercept = CountPixels.line_of_best_fit(weldgap)
 
    # rearrange line equation to give x value
    x = (70 + intercept) // gradient
    x = weldgap_drawing.shape[1] - abs(x)
    print("Weldgap is at:", x)

    CountPixels.draw_line(weldgap_drawing, gradient, intercept, color=(0, 255, 0), thickness=2)
    end_time = time.time()

   # cv2.imshow("DEEZ NUTS" , weldgap_drawing)
   # cv2.waitKey(0)
                                
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return x, weldgap_drawing