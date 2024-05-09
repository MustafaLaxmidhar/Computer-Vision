
from locale import normalize
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
image = cv.imread("WeldGapImages/Set 3/image0301.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

normalized = gray.astype(np.float32) / 255.0
blurred = cv.GaussianBlur(gray, (5,5), 0)

edges = cv.Canny(blurred, 50, 150)

contours, _ = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

weld_gaps = []

min_area_threshold = 100

img = cv.cvtColor(np.float32(image), cv.COLOR_BGR2GRAY)
fft = np.fft.fft2(normalized) #(np.float32(normalized),flags = cv.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft)

magnitude_spectrum = 20*np.log(np.abs(fft_shift))
x, y, z = image.shape
center_x, center_y, center_z = x//2, y//2, z//2 
max_radius = 0.5 * 10 / 2
max_frequency = min(x, y) / 2
radius_frequency = max_radius / max_frequency #/ np.sqrt(x**2 + y**2)
print("Max radius:", max_radius)
print("Max frequency:", max_frequency)
print("Radius frequency:", radius_frequency)
mask = np.zeros((x, y), np.uint8)
for i in range(x):
    for j in range(y):
        distance = np.sqrt((i-center_x)**2 + (j - center_y) ** 2)
        if distance <= radius_frequency * max_frequency:
            mask[i,j] = 1
# cv.circle(mask, (center_x, center_y), radius, 255, -1)
print("Mask shape:", mask.shape)
print("Mask min:", np.min(mask))
print("Mask max:", np.max(mask))
fft_filtered = fft_shift * mask
#filtered_spectrum = magnitude_spectrum * mask
#print("Filtered spectrum min:", np.min(filtered_spectrum))
#print("Filtered spectrum max:", np.max(filtered_spectrum))
filtered_image = np.fft.ifftshift(fft_filtered)
filtered_image = np.fft.ifft2(filtered_image).real
print("Filtered image min:", np.min(filtered_image))
print("Filtered image max:", np.max(filtered_image))
filtered_image_normalized = (filtered_image - np.min(filtered_image)) / (np.max(filtered_image) - np.min(filtered_image))
filtered_image_scaled = (filtered_image_normalized * 255).astype(np.uint8)
#filtered_image_uint8 = cv.convertScaleAbs(filtered_image)
#print("Filtered image uint8 min:", np.min(filtered_image_uint8))
#print("Filtered image uint8 max:", np.max(filtered_image_uint8))
_, thresh = cv.threshold(filtered_image_scaled, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

cv.imshow("Original Image", image)
cv.imshow("Weld Gap", thresh)

cv.waitKey(0)
cv.destroyAllWindows()
#plt.subplot(121),plt.imshow(image, cmap = 'gray')
#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(thresh, cmap = 'gray')
#plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#plt.show()
# for contour in contours:
  #  area = cv2.contourArea(contour)
   # if area < min_area_threshold:
    #    weld_gaps.append(contour)
     #   x, y, w, h = cv2.boundingRect(contour)
      #  cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0))
       # print("Weld Gap position:", x)

#result_image = img.copy()
#cv2.drawContours(result_image, weld_gaps, -1, (0, 255, 0), 2)

#cv2.imshow('identified Weld Gaps', result_image)
#cv2.waitKey(0)

#cv2.destroyAllWindows

