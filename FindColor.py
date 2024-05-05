import cv2
import numpy as np

def most_abundant_colour(image):

    # Calculate the histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Find the index of the most abundant colour
    max_index = np.argmax(hist)

    return max_index

