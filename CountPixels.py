import cv2
import numpy as np

white_pixel_counts = []  # List to store the counts of white pixels in each column

def count_pixels(image):

    for j in range(image.shape[1]):  # Iterate over each column
        white_pixel_count = 0  # Initialize count for the current column
    
        for i in range(image.shape[0]):  # Iterate over each row in the current column
            if image[i, j] > 230:  # Check if the pixel is white
                white_pixel_count += 1  # Increment count if the pixel is white
            
        white_pixel_counts.append(white_pixel_count)  # Add the count for the current column to the list

    image_with_dot = draw_highest_pixel(image, white_pixel_counts)
    return image_with_dot

def draw_highest_pixel(image, white_pixel_counts):
    # Find the index of the column with the highest number of white pixels
    max_count_index = white_pixel_counts.index(max(white_pixel_counts))
    print("max_count_index", max_count_index)

    image_colour = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    # Draw a green dot at the calculated column and y = 70 pixels
    cv2.circle(image_colour, (max_count_index, 70), 1, (0, 255, 0), -1)
    
    return image_colour
    