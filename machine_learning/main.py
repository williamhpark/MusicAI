import numpy as np
import cv2 as cv
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
from preprocessing import preprocessing as pre
from preprocessing import extractDigit as exDig
from preprocessing import extractSquare as exSq

def main(img_Path):
    processedImg, originalImg = pre.process(img_Path,pre.blurImage,pre.thresholdImage,pre.invertImage)
    croppedImg = exSq.prepImg(processedImg,originalImg)
    _ = exSq.extractSquares(croppedImg)

    finalGrid = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            img = cv.imread(currentdir+'\\preprocessing\\extract_cells\\cell_' +
                            str(i)+str(j)+'.jpg', cv.COLOR_BGR2GRAY)
            finalGrid[i].append(exDig.feedDigit(img))
    return finalGrid