import pytesseract
import cv2

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#cv2.IMREAD_GRAYSCALE 조절
#oem, psm 옵션 조절
# cropping = image[100:200, 350:450] #높이를 100~200, 가로를 350~450 사이의 픽셀값을 cropping에 넣었습니다.
# LTSM 비교
config = ('-l kor --oem 1 --psm 4')
im = cv2.imread("test.jpg")
im = im[122:145, 1:246]
cv2.imshow("ori", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(pytesseract.image_to_string(im, config=config))
img_gray = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
img_gray = img_gray[122:145, 1:246]
cv2.imshow("ori_gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(pytesseract.image_to_string(img_gray, config=config))
