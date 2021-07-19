import numpy as np
import cv2


def read_img():
    print("Enter image name: ")
    image_url = input()
    img = cv2.imread(image_url, img=cv2.imread(
        image_url, cv2.IMREAD_GRAYSCALE))
    process = cv2.GaussianBlur(img.copy(), (9, 9), 0)
    process = cv2.adaptiveThreshold(
        process, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    process = cv2.bitwise_not(process, process)
    kernel = np.array([0., 1., 0.], [1., 1., 1.], [0., 1., 0.], np.uint8)
    process = cv2.dilate(process, kernel)
