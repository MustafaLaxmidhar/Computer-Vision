import cv2
import numpy as np

def normalise_histogram(image):
    
    # Calculate the histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Normalize the histogram
    hist_normalized = hist / np.sum(hist)

    return hist_normalized

def most_abundant_colour(histogram):
    
    # Find the index of the most abundant intensity
    max_index = np.argmax(histogram)
    
    # Calculate the intensity value of the most abundant shade1
    most_abundant_intensity = 256 - max_index
    
    return most_abundant_intensity

def increase_contrast(image):
    # Apply contrast stretching
    min_val = np.min(image)
    max_val = np.max(image)
    contrast_stretched = 255 * ((image - min_val) / (max_val - min_val))

    # Convert back to uint8
    contrast_stretched = contrast_stretched.astype(np.uint8)

    return contrast_stretched

