import cv2
import numpy as np
import os
import ColourProcessing 
import ImageCrop
import Threshold
import EdgeDetection
from matplotlib import pyplot as plt

#pathfile for image 
# Define the path to the image and the subfolder
parentfolder = "WeldGapImages"
subfolder = "Set 1"
image_name = "image0001.jpg"  # or whatever the image file name is
src = os.path.join(parentfolder, subfolder, image_name)

# opens image in grayscale
image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

# crop image
x_origin = 0
y_origin = 0
x_width = len(image[1,:])
y_width = 1000   
cropped_image = ImageCrop.crop_image(image, x_origin, y_origin, x_width, y_width)

#increase Contrast of image
contrasted_image = ColourProcessing.increase_contrast(cropped_image)

f = np.fft.fft2(contrasted_image)
fshift = np.fft.fftshift(f)

rows, cols = cropped_image.shape
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_real = np.real(img_back)
img_imag = np.imag(img_back)
img_real = np.uint8(img_real)

# Normalize the real part to the range [0, 255]
fft_real_normalized = cv2.normalize(img_real, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Convert the normalized real part to uint8
fft_real_uint8 = np.uint8(fft_real_normalized)

# Display the uint8 image
cv2.imshow('FFT Real Part (uint8)', fft_real_uint8)
cv2.waitKey(0)




# plt.subplot(121),plt.imshow(cropped_image, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
# plt.show()
