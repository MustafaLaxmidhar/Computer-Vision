import cv2
import numpy as np

def find_consecutive_black_pixels(image, threshold):

    # Get image dimensions
    height, width = image.shape

    # Store the coordinates of consecutive black pixels
    consecutive_pixels_coordinates = []

    # Loop through each row of the image
    for y in range(0, height, 5):
        start = None
        count = 0
        for x in range(width):
            # Check if the pixel is black
            if image[y, x] == 0:
                if start is None:
                    start = x
                count += 1
            else:
                if count >= threshold:
                    # If consecutive black pixels exceed the threshold, store the coordinates
                    middle_x = start + count // 2
                    consecutive_pixels_coordinates.append((middle_x, y))
                start = None
                count = 0

        # Check for consecutive black pixels at the end of the row
        if count >= threshold:
            middle_x = start + count // 2
            consecutive_pixels_coordinates.append((middle_x, y))

    return consecutive_pixels_coordinates

def draw_shapes(image_path, positions):
    # Read the image
    image = cv2.imread(image_path)

    # Draw green circles at each position
    for position in positions:
        x, y = position
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)  # Green color, filled circle

    cv2.line(image, (0, 70), (image.shape[1], 70), (0, 165, 255), 2)

    return image

def find_most_coordinates_range(coordinates, image_width, chunk_width):
    max_coords_count = 0
    best_range = None
    best_coords_in_range = []

    for start_column in range(0, image_width, chunk_width):
        end_column = min(start_column + chunk_width, image_width)
        coords_in_range = [coord for coord in coordinates if start_column <= coord[0] < end_column]
        coords_count = len(coords_in_range)
        if coords_count > max_coords_count:
            max_coords_count = coords_count
            best_range = (start_column, end_column)
            best_coords_in_range = coords_in_range

    return best_coords_in_range

def line_of_best_fit(coordinates):
    # Extract x and y coordinates separately
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # Fit a polynomial of degree 1 (line) to the data
    coefficients = np.polyfit(x_values, y_values, 1)

    # Extract slope (m) and y-intercept (b)
    m = coefficients[0]
    b = coefficients[1]

    return m, b

def draw_line(image, m, b, color=(0, 255, 0), thickness=2):
    height, width, _ = image.shape
    y1 = int(m * 0 + b)  # Calculate y-coordinate for x=0 (left edge)
    y2 = int(m * width + b)  # Calculate y-coordinate for x=width (right edge)
    cv2.line(image, (0, y1), (width, y2), color, thickness)