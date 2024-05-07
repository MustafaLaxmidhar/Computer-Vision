import cv2
import os

def find_vertical_lines(image):
    
    # Apply Sobel filter in the vertical direction
    sobel_vertical = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Threshold the result to obtain binary image
    _, binary_vertical = cv2.threshold(cv2.convertScaleAbs(sobel_vertical), 10, 255, cv2.THRESH_BINARY)
    
    return binary_vertical

def find_edges(image):
    # Convert the image to grayscale
    
    # Apply Canny edge detection
    edges = cv2.Canny(image, 120, 135)  # Adjust threshold values as needed
    
    return edges

