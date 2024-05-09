import cv2
import np

def find_weldgap_positions(image):
    
    # Get the height of the image
    height = image.shape[0]
    
    # Initialize an array to store weld gap positions
    weldgap_positions = []
    
    # Iterate through each row of the image
    for y in range(height):
        row = image[y, :]  # Get the row of pixels
        
        # Check if there are any black pixels (pixel value = 0) in the row
        if np.any(row == 0):
            # Find the indices of the first and last black pixel in the row
            first_black_pixel = np.argmax(row == 0)
            last_black_pixel = len(row) - np.argmax(row[::-1] == 0) - 1

            # Calculate the average position of the weld gap
            avg_position = (first_black_pixel + last_black_pixel) / 2
        else:
            # If there are no black pixels in the row, set avg_position to -1
            avg_position = -1
        
        # Append the average position to the weldgap_positions array
        weldgap_positions.append(avg_position)
    
    return weldgap_positions

def line_of_best_fit(weldgap_positions, y):
    # Perform linear regression using numpy's polyfit function
    coefficients = np.polyfit(weldgap_positions, y, 1)
    
    # Get the slope and intercept of the line
    slope, intercept = coefficients
    
    return slope, intercept
