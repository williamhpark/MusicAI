import cv2 as cv
import numpy as np
import PreProcessing as pre


def findContours(img):
    """Find the contours of the board"""
    contours, heirarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    return contours


def findCorners(ext_contours):
    """Find the corners of the largest sudoku board"""
    for i  in ext_contours:
        peri = cv.arcLength(i,True)
        approx = cv.approxPolyDP(i,0.015*peri,True)
        if len(approx) == 4:
            return approx


def extractCorners(corners):
    """Take out the (x,y) coordinates from the corner list"""
    corners = [(corner[0][0],corner[0][1])for corner in corners]
    top_l,bottom_l,bottom_r,top_r = corners[0],corners[1],corners[2],corners[3]
    return top_l,top_r,bottom_r,bottom_l


def calcDist(pt1,pt2):
    """Distance function between two points"""
    return np.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2))


def calcWidth(top_r,top_l,bottom_l,bottom_r):
    """Calculate and return the largest width between the top and bottom"""
    width_A = calcDist(bottom_r,bottom_l)
    width_B = calcDist(top_r,top_l)
    return max(int(width_A),int(width_B))


def calcHeight(top_r,top_l,bottom_l,bottom_r):
    """Calculate and return the largest height between the right and left"""
    height_A = calcDist(top_r,bottom_r)
    height_B = calcDist(top_l,bottom_l)
    return max(int(height_A),int(height_B))


def cropWarp(img,width,height,corners):
    """Crop and warp image for perspectives that are not front facing"""
    dimensions = np.array([[0,0],[width-1,0],[width-1,height-1],[0,height-1]],dtype='float32')
    ordered_corners = np.array(corners,dtype='float32')
    grid = cv.getPerspectiveTransform(ordered_corners,dimensions)
    return cv.warpPerspective(img,grid,(width,height))

def extractSquares(cropped_img):
    """Extract squares and save as JPG"""
    # Convert color image to gray again
    # Apparently image is already in gray???
    # grid = cv.cvtColor(cropped_img,cv.COLOR_BGR2GRAY)
    # Invert and apply gaussian thresholding again before extraction
    grid = cv.bitwise_not(cv.adaptiveThreshold(cropped_img,255,
                                cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,101,1)) 


    # Divide the image equally into 9 parts vertically and horizontally
    edge_h = np.shape(grid)[0]
    edge_w = np.shape(grid)[1]
    celledge_h = edge_h//9
    celledge_w = edge_w//9


    tempgrid = []
    for i in range(celledge_h,edge_h+1,celledge_h):
        for j in range(celledge_w,edge_w+1,celledge_w):
            rows = grid[i-celledge_h:i]
            tempgrid.append([rows[k][j-celledge_w:j] for k in range(len(rows))])

    finalgrid = []
    for i in range(0,len(tempgrid)-8,9):
        finalgrid.append(tempgrid[i:i+9])

    for i in range(9):
        for j in range(9):
            finalgrid[i][j] = np.array(finalgrid[i][j])
    for i in range(9):
        for j in range(9):
            cv.imwrite(str("machine_learning/extract_cells/cell_"+str(i)+str(j)+".jpg"),finalgrid[i][j])
    
    return finalgrid


"""FOR TESTING"""
# Pre-process Image
# img,original = pre.process("machine_learning/preprocessing/Photos/sudoku_board.jpg", 
#                     blur = pre.blurImage, threshold= pre.thresholdImage, inversion = pre.invertImage)

# cv.imshow('Orignal', original)
# cv.imshow('Processed Image', img)
# cv.waitKey(0)

# contours = findContours(img)

# # Draw Contours
# contour_img = np.zeros((img.shape[0],img.shape[1],3))
# cv.drawContours(contour_img,contours,-1,(0,255,0),1)
# cv.imshow('Contours',contour_img)

# corners = findCorners(contours)

# Draw Corners
# corner_img = np.zeros((img.shape[0],img.shape[1],3))
# cv.drawContours(corner_img,corners,-1,(0,255,0),10)
# cv.imshow('Corners',corner_img)
# cv.waitKey(0)

# Crop and warp Image
# ordered_corners = extractCorners(corners)
# width = calcWidth(*ordered_corners)
# height = calcHeight(*ordered_corners)
# cropped_img = cropWarp(original,width,height,ordered_corners)
# cv.imshow('Cropped Image', cropped_img)
# cv.waitKey(0)

# Extract Squares and save as JPG
# grid = extractSquares(cropped_img)
