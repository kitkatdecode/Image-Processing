import cv2
import numpy as np
import pywt
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
# wavelet transform
dec_lo = [-.25, .5, 1.5, .5, -.25]
dec_hi = [0, .25, -.5, .25, 0]
rec_lo = [0, .25, .5, .25, 0]
rec_hi = [.25, .5, -1.5, .5, .25]
filter_bank = [dec_lo, dec_hi, rec_lo, rec_hi]

myWavelet = pywt.Wavelet(name="BiorthWavelet", filter_bank=filter_bank)

def analysis(img, show=False):
    cA, (cH,cV,cD) = pywt.dwt2(img, myWavelet)
    
    if show:
        cA1 = np.uint8(cA)
        cH1 = np.uint8(cH)
        cV1 = np.uint8(cV)
        cD1 = np.uint8(cD)
        cA1 = cv2.resize(cA1, FRAME_SIZE)
        cH1 = cv2.resize(cH1, FRAME_SIZE)
        cV1 = cv2.resize(cV1, FRAME_SIZE)
        cD1 = cv2.resize(cD1, FRAME_SIZE)
        cv2.imshow("low-low",cA1)
        cv2.imshow("low-high",cH1)
        cv2.imshow("high-low",cV1)
        cv2.imshow("high-high",cD1)
        
    return cA, cH, cV, cD

def synthesis(cA, cD):
    img = pywt.idwt2((cA,cD), myWavelet)
    img = np.uint8(img)
    img1 = cv2.resize(img, FRAME_SIZE)
    cv2.imshow("After synthesis",img1)
    return img

def thresholding(img,t):
    img1 = pywt.threshold(img,t,mode="soft") 
    # ret, t2 = cv2.threshold(img, t, 255, cv2.THRESH_TOZERO_INV)
    
    # img1 = np.uint8(img1)
    
    return img1
    
# img in BGR format
img = cv2.imread("./Crane.JPG")

imgGray = toGray(img)
noisy = addNoise(imgGray, 0, SIGMA)

threshold = int(input("Enter threshold value: "))

# analysis
cA, cH, cV, cD = analysis(noisy, True)

# thresholding
cA = thresholding(cA, threshold)
cH = thresholding(cH, threshold)
cV = thresholding(cV, threshold)
cD = thresholding(cD, threshold)

# synthesis
filtered = synthesis(cA,(cH,cV,cD))

def PSNR(original, derived): 
    mse = np.mean((original - derived) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse)) 
    return psnr

# PSNR wrt noisy image and filtered image

psnr_noisy = PSNR(imgGray, noisy)
psnr_filtered = PSNR(imgGray,filtered)

print("PSNR w.r.t. noisy image = "+str(psnr_noisy))
print("PSNR w.r.t. filtered image = "+str(psnr_filtered))


# resize to show the image within frame
imgGray = cv2.resize(imgGray, FRAME_SIZE)
noisy = cv2.resize(noisy, FRAME_SIZE)


cv2.imshow("Noisy Image",noisy)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


#%%
