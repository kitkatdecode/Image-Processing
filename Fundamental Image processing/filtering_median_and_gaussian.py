import cv2
import numpy as np
import math
#%%

FRAME_SIZE = (1000,800)
SIGMA = 5 # standard deviation for noise

# function changing image to grayscale
def toGray(img):
    imgGray = np.dot(img[...,:3], [.3,.59,.11])
    # imgGray = .3*img[:,:,0]+.59*img[:,:,1]+.11*img[:,:,2]
    imgGray = np.uint8(imgGray)
    return imgGray

def addNoise(img, mean, sigma):
    gauss = np.random.normal(mean,sigma,img.shape)
    gauss = gauss.reshape(img.shape)
    noisy = img + gauss
    noisy = np.uint8(noisy)
    return noisy

#####################
    
# img in BGR format
img = cv2.imread("./Crane.JPG")

imgGray = toGray(img)
noisy = addNoise(imgGray, 0, SIGMA)

# median filtering
median_filtered = cv2.medianBlur(noisy,9)

# gaussian filtering
gauss_filtered = cv2.GaussianBlur(noisy,(9,9),4)



def PSNR(original, derived): 
    mse = np.mean((original - derived) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse)) 
    return psnr

# PSNR wrt noisy image and filtered image

psnr_median = PSNR(imgGray, median_filtered)
psnr_gauss = PSNR(imgGray,gauss_filtered)

print("PSNR w.r.t. median filtering image = "+str(psnr_median))
print("PSNR w.r.t. gaussian filtering image = "+str(psnr_gauss))


# resize to show the image within frame]
imgGray = cv2.resize(imgGray, FRAME_SIZE)
noisy = cv2.resize(noisy, FRAME_SIZE)
median_filtered = cv2.resize(median_filtered, FRAME_SIZE)
gauss_filtered = cv2.resize(gauss_filtered, FRAME_SIZE)

cv2.imshow("Noisy Image",noisy)
cv2.imshow("median_filtered Image",median_filtered)
cv2.imshow("gauss_filtered Image",gauss_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


#%%
