#Author: Ori Weiss
#Version: 1.0
import cv2
import numpy as np
from skimage.feature import canny
from scipy import ndimage as ndi
import math




def image_prep(path):
    mask_size = 400
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    edges = canny(img/255.)
    fill_img = ndi.binary_fill_holes(edges)
    label_objects, nb_labels = ndi.label(fill_img)
    sizes = np.bincount(label_objects.ravel())
    mask_sizes = sizes > mask_size
    mask_sizes[0] = 0
    img_cleaned = mask_sizes[label_objects]
    labeled_img, num_features = ndi.label(img_cleaned)
    return labeled_img, num_features

def numofneighbour(mat, i, j, searchValue):
    count = 0;

    # UP
    if (i > 0 and mat[i - 1][j] == searchValue):
        count += 1;

        # LEFT
    if (j > 0 and mat[i][j - 1] == searchValue):
        count += 1;

        # DOWN
    if (i < len(mat) - 1 and mat[i + 1][j] == searchValue):
        count += 1

    # RIGHT
    if (j < len(mat[i]) - 1 and mat[i][j + 1] == searchValue):
        count += 1;

    return count;


# Returns sum of perimeter of shapes formed with 1s
def findperimeter(mat, num_features):
    perimeter = [0] * (num_features+1)

    # Traversing the matrix and finding ones to
    # calculate their contribution.
    for i in range(len(mat)):
        for j in range(0, len(mat[i])):
            if (mat[i][j] != 0):
                perimeter[mat[i][j]] += (4 - numofneighbour(mat, i, j, mat[i][j]))

    return perimeter
def extract_area_perim(img,num_features):
    area = [0] * (num_features+1)
    for i in range(len(img)):
        for j in range(len(img[i])):
            value = img[i][j]
            if(value != 0):
                area[value]+=1
    return area, findperimeter(img,num_features)

def extract_circularity(area, perimeter):
    circularity = [0] * (len(area))
    for i in range(len(area)):
        circularity[i] = 4 * (math.pi * area[i])/(math.pow(perimeter[i],2))
    return circularity

def convert_to_relative(cellAreas, cellPerims):
    averageCellSize = np.mean(cellAreas)
    averagePerimSize = np.mean(cellPerims)
    relativeArea = [0] * len(cellAreas)
    relativePerim = [0] * len(cellPerims)
    for i in range(len(cellAreas)):
        relativeArea[i] = cellAreas[i]/averageCellSize
        relativePerim[i] = cellPerims[i] / averagePerimSize
    return relativeArea, relativePerim

def removeFromImg(img, feature):
    for i in range(len(img)):
        for j in range(0, len(img[i])):
            if (img[i][j] == feature):
                img[i][j] = 0
    return img


def removeOutliers(area, perim, img):
    mean = np.mean(area)
    std = np.std(area)
    for i in range(len(area) - 1, -1, -1):
        if mean+3.5*std < area[i]:
            print("Popping feature: ", i)
            area.pop(i)
            perim.pop(i)
            img = removeFromImg(img, i+1)
    return area, perim, img

