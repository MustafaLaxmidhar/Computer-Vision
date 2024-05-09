import cv2
import numpy as np

black_pixel_counts = []  # List to store the counts of white pixels in each column

def count_pixels(image):

    for j in range(image.shape[1]):  # Iterate over each column
        black_pixel_count = 0  # Initialize count for the current column
    
        for i in range(image.shape[0]):  # Iterate over each row in the current column
            if image[i, j] ==  0:  # Check if the pixel is BLACK
                black_pixel_count += 1  # Increment count if the pixel is BLACK
            
        black_pixel_counts.append(black_pixel_count)  # Add the count for the current column to the list

    return black_pixel_counts

def draw_highest_pixel(image, pixel_counts):

    # Find the index of the column with the highest number of BLACK pixels
    max_count_index = pixel_counts.index(max(pixel_counts))
    print(type(max_count_index))
    print("max_count_index:", max_count_index)

    image_colour = cv2.imread(image, cv2.COLOR_GRAY2BGR)
    
    # Draw a green dot at the calculated column and y = 70 pixels
    cv2.line(image_colour, (0, 70), (image_colour.shape[1], 70), (0, 255, 0), thickness=1)
    cv2.line(image_colour, (0, max_count_index), (image_colour.shape[1], max_count_index), (0, 255, 0), thickness=1)
    
    return image_colour
    