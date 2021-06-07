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
img = cv2.imread("C:/Users/ASUS/Pictures/signatures/IMG_1761.jpg")#("./Crane.JPG")#

imgGray = toGray(img)

# histogram equalization
equilized_img = cv2.equalizeHist(imgGray)

# Otsu thresholding
ret, threshold_img = cv2.threshold(equilized_img, 0, 255, cv2.THRESH_OTSU)

print("Computed threshold: "+str(ret))
cv2.imwrite("Gray.jpg",cv2.GaussianBlur(imgGray, (9,9), 4))
imgGray = cv2.resize(imgGray, FRAME_SIZE)
equilized_img = cv2.resize(equilized_img, FRAME_SIZE)
threshold_img = cv2.resize(threshold_img, FRAME_SIZE)

cv2.imshow("Original Gray Image",imgGray)
cv2.imshow("Equalized Image",equilized_img)
cv2.imshow("Thresholded Image",threshold_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
