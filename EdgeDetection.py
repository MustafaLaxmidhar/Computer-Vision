import cv2
import os

# Function to perform edge detection with variable threshold
def edge_detection(image, min_threshold, max_threshold):
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (9, 3), 0)
    
    # Perform Canny edge detection with variable threshold
    edges = cv2.Canny(blurred, min_threshold, max_threshold)
    
    return edges

#pathfile for image 
# Define the path to the image and the subfolder
subfolder = "Set3"
image_name = "image0300.jpg"  # or whatever the image file name is
src = os.path.join(subfolder, image_name)

image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

# Set initial threshold values
min_threshold = 90
max_threshold = 100

# Perform edge detection with initial threshold values
edges = edge_detection(image, min_threshold, max_threshold)

# Display the result
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
