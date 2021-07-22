import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2 as cv
import sys
sys.path.append("./machine_learning")
import LoadModel as load


def findDigit(img):
    """Find the digit and return a resized numpy array of dimension 28x28"""
    thresh = 128
    dimensions = (28, 28)
    border = 25
    gray = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    contours = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    ROI = None
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)

        if(x < 3 or y < 3 or w < 3 or h < 3):
            continue
        ROI = gray[y:y+h, x:x+w]

    if ROI is not None:
        ROI = cv.copyMakeBorder(ROI, border, border,
                                border, border, cv.BORDER_CONSTANT)
        return cv.resize(ROI, dimensions)
    else:
        return None


def feedDigit(img):
    """Extract digit and convert to dimension 1x1x28x28 then feed to model"""
    ROI = findDigit(img)
    if ROI is not None:
        xb = (torch.from_numpy(ROI).unsqueeze(0).unsqueeze(0))/255
        yb = load.model(xb)
        _, preds = torch.max(yb, dim=1)
        # plt.imshow(ROI,cmap='Greys')
        # plt.suptitle(f'Prediction: {preds[0].item()}')
        # plt.show()
        return preds[0].item()
    else:
        return None


"""FOR TESTING"""
# img = cv.imread('machine_learning/preprocessing/extract_cells/cell_13.jpg',cv.COLOR_BGR2GRAY)
# print(extractDigit(img))
# tempgrid = []
# for i in range(9):
#     for j in range(9):
#         img = cv.imread('machine_learning/preprocessing/extract_cells/cell_' +
#                         str(i)+str(j)+'.jpg', cv.COLOR_BGR2GRAY)
#         tempgrid.append(feedDigit(img))

# print(tempgrid)
