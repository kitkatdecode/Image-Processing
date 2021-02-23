import cv2
import numpy as np


FRAME_SIZE = (1000,800)

# function changing image to grayscale
def toGray(img):
    imgGray = np.dot(img[...,:3], [.3,.59,.11])
    # imgGray = .3*img[:,:,0]+.59*img[:,:,1]+.11*img[:,:,2]
    imgGray = np.uint8(imgGray)
    return imgGray

# img in BGR format
img = cv2.imread("./Crane.JPG")

imgGray = toGray(img)

grayFloat = np.float32(imgGray)
corner_detected = cv2.cornerHarris(grayFloat,3,3,0.04)

#result is dilated for marking the corners
corner_detected = cv2.dilate(corner_detected,None)

imgGray[corner_detected > 0.01 * corner_detected.max()]=0

corner_detected = cv2.resize(corner_detected, FRAME_SIZE)
imgGray = cv2.resize(imgGray, FRAME_SIZE)

cv2.imshow("Gray Image with corners in Black",imgGray)
cv2.imshow("corner_detected Image",corner_detected)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
