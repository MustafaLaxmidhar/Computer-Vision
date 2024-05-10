import cv2
import numpy as np
import os
import ColourProcessing 
import ImageCrop
import Threshold
from matplotlib import pyplot as plt

#pathfile for image 
# Define the path to the image and the subfolder
parentfolder = "WeldGapImages"
subfolder = "Set 3"
image_name = "image0300.jpg"  # or whatever the image file name is
src = os.path.join(parentfolder, subfolder, image_name)

def image_processing(image_path):

    # opens image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    #increase Contrast of image
    contrasted_image = ColourProcessing.increase_contrast(image)

    # Apply a gaussian filter
    gaussian_image = cv2.GaussianBlur(contrasted_image, (5, 5), 0)

    f = np.fft.fft2(gaussian_image)
    fshift = np.fft.fftshift(f)

    #implement High pass filter
    rows, cols = contrasted_image.shape
    crow, ccol = rows//2, cols//2
    fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_real = np.real(img_back)

    # Normalize the real part to the range [0, 255]
    fft_real_normalized = cv2.normalize(img_real, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Convert the normalized real part to uint8
    fft_real_uint8 = np.uint8(fft_real_normalized)


    # Apply a bilateral filter
    blf_image = cv2.bilateralFilter(fft_real_uint8, d = 5, sigmaColor = 75, sigmaSpace = 75)


    # Apply a threshold on the most common colour in the image
    histogram = ColourProcessing.normalise_histogram(blf_image)
    intial_threshold = ColourProcessing.most_abundant_colour(histogram)

    # crop image
    x_origin = 0
    y_origin = 0
    x_width = len(image[1,:]) - 20
    y_width = 140   
    cropped_image = ImageCrop.crop_image(blf_image, x_origin, y_origin, x_width, y_width)


    # Apply variable threshold function
    final_threshold = Threshold.find_threshold(cropped_image, 2000, 100)
    ret, final_image = cv2.threshold(cropped_image, final_threshold, 255, cv2.THRESH_BINARY)

    return final_image


