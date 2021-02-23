import cv2
import numpy as np


FRAME_SIZE = (1000,800)
SIGMA = 4


# function changing image to grayscale
def toGray(img):
    imgGray = np.dot(img[...,:3], [.3,.59,.11])
    # imgGray = .3*img[:,:,0]+.59*img[:,:,1]+.11*img[:,:,2]
    imgGray = np.uint8(imgGray)
    return imgGray

# img in BGR format
img = cv2.imread("./Crane.JPG")

imgGray = toGray(img)

def laplace_of_gaussian(gray_img, sigma=1.):
    
    img1 = cv2.GaussianBlur(gray_img, (9, 9), sigma)
    log = cv2.Laplacian(img1, cv2.CV_64F)
    return log
    
def zeroCrossing(log):
    rows, cols = log.shape[:2]
    
    # min/max of 3x3-neighbourhoods
    min_map = np.minimum.reduce(list(log[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    max_map = np.maximum.reduce(list(log[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    
    # bool matrix for image value positive
    pos_img = 0 < log[1:rows-1, 1:cols-1]
    # bool matrix for min < 0 and 0 < image pixel
    neg_min = min_map < 0
    neg_min[1 - pos_img] = 0
    # bool matrix for 0 < max and image pixel < 0
    pos_max = 0 < max_map
    pos_max[pos_img] = 0
    
    # sign change at pixel
    zero_cross = neg_min + pos_max
    
    # values: max - min, scaled to 0--255; set to 0 for no sign change
    scale = 255. / max(1., log.max() - log.min())
    img = scale * (max_map - min_map)
    img[1 - zero_cross] = 0.
    
    zeroCross =np.uint8(img)
    return zeroCross

# LoG image
log_img = laplace_of_gaussian(imgGray,SIGMA)
print("LoG Done")

# zeroCrossing image
zeroCross = zeroCrossing(log_img)
print("Zero-Crossing done")

imgGray = cv2.resize(imgGray, FRAME_SIZE)
log_img = cv2.resize(log_img, FRAME_SIZE)
zeroCross = cv2.resize(zeroCross, FRAME_SIZE)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("log_img Image",log_img)
cv2.imshow("zeroCross Image",zeroCross)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
