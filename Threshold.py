import cv2

def find_threshold (image, num_pixels, start_threshold):
    
    black_pixel_count = 0
    threshold = start_threshold

    while (abs(black_pixel_count - num_pixels) > 50):

        if threshold % 2 == 0:
            prev_threshold = threshold
        
        # Apply thresholding
        maxval = 255 
        retval, output = cv2.threshold(image, threshold, maxval, cv2.THRESH_BINARY)

        # Count the number of black pixels
        black_pixel_count = (len(image[1,:]) * len(image[:,1])) - cv2.countNonZero(output)

        # Increment threshold value
        if black_pixel_count < num_pixels:
            threshold += 1
        else:
            threshold -= 1

        if threshold == prev_threshold:
            return threshold
        
        

    return threshold

