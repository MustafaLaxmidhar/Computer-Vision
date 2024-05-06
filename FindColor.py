import cv2
import numpy as np

def most_abundant_colour(image):

    # Calculate the histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Find the index of the most abundant intensity
    max_index = np.argmax(hist)
    
    # Calculate the intensity value of the most abundant shade
    most_abundant_intensity = 256 - max_index
    
    return most_abundant_intensity

