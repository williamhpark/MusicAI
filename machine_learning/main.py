from machine_learning.preprocessing.PreProcessing import blurImage
import numpy as np
import cv2 as cv
import preprocessing.PreProcessing as pre
import preprocessing.ExtractDigit as exDig
import preprocessing.ExtractSquare as exSq

def main():
    processedImg, originalImg = pre.process(img,pre.blurImage,pre.thresholdImage,pre.invertImage)
    croppedImg = exSq.prepImg(processedImg,originalImg)
    _ = exSq.extractSquares(croppedImg)

    finalGrid = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            img = cv.imread('machine_learning/preprocessing/extract_cells/cell_' +
                            str(i)+str(j)+'.jpg', cv.COLOR_BGR2GRAY)
            finalGrid[i].append(exDig.feedDigit(img))
    return finalGrid



if __name__=="__main__":
    main()