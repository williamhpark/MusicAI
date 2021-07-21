from PIL.Image import NONE
import numpy as np
import torch
import cv2 as cv
import sys
sys.path.append("./machine_learning")
import LoadModel as load
import matplotlib.pyplot as plt

def extractDigit(img):
    thresh = 128
    tmp_sudoku = []
    dimensions = (28,28)
    border = 20
    gray = cv.threshold(img,thresh,255,cv.THRESH_BINARY)[1]
    contours = cv.findContours(gray,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]  
    ROI = None
    for contour in contours:
        x,y,w,h = cv.boundingRect(contour)

        if(x<3 or y<3 or w<3 or h<3):
            continue
        ROI = gray[y:y+h,x:x+w]
    if ROI is not None:
        ROI = cv.copyMakeBorder(ROI,border,border,border,border,cv.BORDER_CONSTANT)
        ROI = cv.resize(ROI,dimensions)
        xb = (torch.from_numpy(ROI).unsqueeze(0).unsqueeze(0))/255
        yb = load.model(xb)
        _,preds = torch.max(yb,dim=1)
        # plt.imshow(ROI,cmap='Greys')
        # plt.suptitle(f'Prediction: {preds[0].item()}')
        # plt.show()
        return preds[0].item()
    else:
        return 0


"""FOR TESTING"""
# img = cv.imread('machine_learning/preprocessing/extract_cells/cell_13.jpg',cv.COLOR_BGR2GRAY)
# print(extractDigit(img))
tempgrid = []
for i in range(9):
    for j in range(9):
        img = cv.imread('machine_learning/preprocessing/extract_cells/cell_'+str(i)+str(j)+'.jpg',cv.COLOR_BGR2GRAY)
        tempgrid.append(extractDigit(img))

print(tempgrid)