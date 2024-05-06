import cv2

def crop_image(image, x, y, width, height):

    # Crop the image
    cropped_image = image[y:y+height, x:x+width]

    return cropped_image