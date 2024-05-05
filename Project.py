import cv2
import numpy
img = cv2.imread("WeldGapImages/Set 1/image0003.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

weld_gaps = []

min_area_threshold = 100

for contour in contours:
    area = cv2.contourArea(contour)
    if area < min_area_threshold:
        weld_gaps.append(contour)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0))
        print("Weld Gap position:", x)

result_image = img.copy()
cv2.drawContours(result_image, weld_gaps, -1, (0, 255, 0), 2)

cv2.imshow('identified Weld Gaps', result_image)
cv2.waitKey(0)

cv2.destroyAllWindows

