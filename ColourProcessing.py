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

# def increase_contrast(image):
#     # Apply contrast stretching
#     min_val = np.min(image)
#     print("min_val", min_val)
#     max_val = np.max(image)
#     contrast_stretched = 255 * ((image - min_val) / (max_val - min_val))


#     # Convert back to uint8
#     contrast_stretched = contrast_stretched.astype(np.uint8)

#     return contrast_stretched

def increase_contrast(image):
    # Apply contrast stretching
    min_val = np.min(image)
    max_val = np.max(image)
    
    # Apply a non-linear transformation to amplify contrast
    contrast_stretched = 255 * ((image - min_val) / (max_val - min_val)) ** 1.5

    # Clip values to ensure they are within the valid range [0, 255]
    contrast_stretched = np.clip(contrast_stretched, 0, 255)

    # Convert back to uint8
    contrast_stretched = contrast_stretched.astype(np.uint8)

    return contrast_stretched


import cv2

# Load the image in grayscale
def add_dark(image):

    # Iterate through each pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Check if pixel intensity is greater than 5
            if image[i, j] < 20:
                # Set pixel intensity to a lower value
                image[i, j] = 0

    # Display the modified image
    #cv2.imshow("dark Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return image

def remove_light(image):

    # Iterate through each pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Check if pixel intensity is greater than 5
            if image[i, j] > 20:
                # Set pixel intensity to a lower value
                image[i, j] = 254

    # Display the modified image
    # cv2.imshow("light Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return image
