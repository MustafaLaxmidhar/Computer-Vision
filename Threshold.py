import cv2
import numpy as np

def find_threshold (image, num_pixels, start_threshold):
    
    black_pixel_count = 0
    threshold = start_threshold

    while (abs(black_pixel_count - num_pixels) > 100):
    
        # Apply thresholding
        maxval = 255 
        retval, output = cv2.threshold(image, threshold, maxval, cv2.THRESH_BINARY)

        # Count the number of black pixels
        black_pixel_count = 120000 - cv2.countNonZero(output)
        print("Number of black pixels: " + str(black_pixel_count))

        # Increment threshold value
        if black_pixel_count < num_pixels:
            threshold += 1
        else:
            threshold -= 1
        
        
    
    print(str(threshold))
    return threshold

