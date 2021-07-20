import cv2 as cv
import numpy as np


def rescaleImage(img, scale=0.75):
    """Rescale image"""
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)



def grayscaleImage(img_Path):
    """Apply grayscale onto image and then rescale"""
    img = cv.imread(str(img_Path), cv.IMREAD_GRAYSCALE)
    img = rescaleImage(img, scale=0.4)

    # Show image if wanted
    # cv.imshow('Grayscale Resized Image', img)
    # cv.waitKey(0)
    return img


def blurImage(img):
    """Apply Gaussian blurring on image"""
    out = cv.GaussianBlur(img, (9, 9), 0,)

    # cv.imshow('Gaussian Blur', out)
    # cv.waitKey(0)
    return out


def thresholdImage(img):
    """Adaptive Gaussian Thresholding"""
    out = cv.adaptiveThreshold(
        img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    # cv.imshow('Gaussian Thresholding', out)
    # cv.waitKey(0)
    return out


def invertImage(img):
    """Invert and dilate image"""
    invert = cv.bitwise_not(img, img)
    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
    out = cv.dilate(invert, kernel)
    
    # cv.imshow('Inverted and Dilated Image', out)
    # cv.waitKey(0)
    return out

def process(img_Path, blur = None ,threshold = None, inversion = None):
    img = grayscaleImage(img_Path)
    if blur is not None:
        processBlur = blur(img)
    if threshold is not None:
        processThreshold = threshold(processBlur)
    if inversion is not None:
        out = inversion(processThreshold)
    return out
    
    
"""FOR TESTING"""


# img = process('Pre-Processing/Photos/sudoku_board.jpg', blurImage, thresholdImage, invertImage) 
