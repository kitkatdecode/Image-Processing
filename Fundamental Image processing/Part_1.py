import cv2
import numpy as np

#%%

# function changing image to grayscale
def toGray(img):
    imgGray = np.dot(img[...,:3], [.3,.59,.11])
    # imgGray = .3*img[:,:,0]+.59*img[:,:,1]+.11*img[:,:,2]
    imgGray = np.uint8(imgGray)
    return imgGray

# img in BGR format
img = cv2.imread("./Crane.JPG")

# can also use inbuilt function in opencv
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgGray = toGray(img)

# resize to show the image within frame
imgGray = cv2.resize(imgGray, (960, 600))
img = cv2.resize(img, (960, 600))

# showing the image
original = "Original Image"
gray = "Grayscale Image"
cv2.namedWindow(original)

cv2.namedWindow(gray)

cv2.imshow(original,img)
cv2.imshow(gray,imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
