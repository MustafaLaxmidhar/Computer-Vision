import cv2

def crop_image(image_path, x, y, width, height):
    # Read the image
    image = cv2.imread(image_path)

    # Crop the image
    cropped_image = image[y:y+height, x:x+width]

    return cropped_image