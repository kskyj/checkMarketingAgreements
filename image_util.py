import cv2
import pyautogui
import matplotlib.pyplot as plt


def view_cropped_img(filename, start_x, start_y, end_x, end_y):
    img = plt.imread(filename)
    # [y:y+h, x:x+w]
    img_cropped = img[start_y:end_y, start_x:start_y]

    cv2.imshow("cropped", img_cropped)
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def view_img(filename):
    img = plt.imread(filename)
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.show()


def cv2_view_img(filename, option=None):
    img = cv2.imread(filename, option)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 스크린 샷 찍기
    # img1 = pyautogui.screenshot()
    # img2 = pyautogui.screenshot('screenshot_test.png')
    # img3 = pyautogui.screenshot('screenshot_test.png', region=(0, 0, 300, 300))
    # filename = 'E:/dev/vsc_workspace/python/opencv/marketingAgreementInspection/test/test3.jpg'
    # view_cropped_img(filename, 365, 705, 569, 732)

    # pyautogui.screenshot('screenshot_test.png', region=(0, 0, 500, 300))
    # view_img('screenshot_test.png')
    cv2_view_img('test.jpg',  cv2.IMREAD_GRAYSCALE)
