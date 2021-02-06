import cv2

# Load image, convert to grayscale, Otsu's threshold
image = cv2.imread("E:/dev/vsc_workspace/python/opencv/test3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours, filter using contour approximation, aspect ratio, and contour area
threshold_max_area = 550
threshold_min_area = 100
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.035 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = w / float(h)
    area = cv2.contourArea(c)
    if len(approx) == 4 and area < threshold_max_area and area > threshold_min_area and (aspect_ratio >= 0.9 and aspect_ratio <= 1.1):
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)

cv2.imshow("image", image)
cv2.imshow("thresh", thresh)
cv2.waitKey()
