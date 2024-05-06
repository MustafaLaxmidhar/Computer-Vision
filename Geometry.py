import cv2

def find_weldgap_width(image):

    #checks the maximum width of the weldgap
    #adjusts the threshold accordingly

    for i in range(140):
        #if the width exceeds max, decrease threshold
        width = count_consecutive_black_pixels_in_row(image, i)
        if width 

def count_consecutive_black_pixels_in_row(image, row_index):
    # Get the number of columns (width) in the image
    num_columns = image.shape[1]
    
    # Initialize a counter for consecutive black pixels
    consecutive_black_pixel_count = 0
    max_consecutive_black_pixel_count = 0
    
    # Iterate over each column in the specified row
    for col_index in range(num_columns):
        # Get the intensity value of the pixel at (row_index, col_index)
        pixel_intensity = image[row_index, col_index]
        
        # Check if the pixel is black (intensity = 0)
        if pixel_intensity == 0:
            consecutive_black_pixel_count += 1
        else:
            # Reset the consecutive count if a non-black pixel is encountered
            max_consecutive_black_pixel_count = max(max_consecutive_black_pixel_count, consecutive_black_pixel_count)
            consecutive_black_pixel_count = 0
    
    # Check if the last sequence of black pixels extends to the end of the row
    max_consecutive_black_pixel_count = max(max_consecutive_black_pixel_count, consecutive_black_pixel_count)
    
    return max_consecutive_black_pixel_count