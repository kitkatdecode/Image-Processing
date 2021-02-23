"""
@author: Kartik Saini

"""

"""
@author: Kartik Saini

"""

#%%

# importing tkinter gui 
import tkinter as tk 
import cv2
import numpy as np
from PIL import ImageTk, Image
from functools import partial

#%%
canvasG = None
window_width = None
window_height = None
drawLine = False
img_w = None
img_h = None

x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0

ix1 = 0
iy1 = 0
ix2 = 0
iy2 = 0
ix3 = 0
iy3 = 0

inA = False
inB = False
inC = False

imageA = None
imageB = None
imageC = None

matchesAB_A = []
matchesAB_B = []

matchesAC_A = []
matchesAC_C = []

imageALoaded = False
imageBLoaded = False
imageCLoaded = False

def selectGlobalCanvas(event):
    global imageALoaded, imageBLoaded, imageCLoaded
    
    if imageALoaded == False or imageBLoaded == False or imageCLoaded == False:
        return
    
    global x1,y1,x2,y2,x3,y3, ix1, iy1, ix2, iy2,ix3,iy3, matchesAB_A, matchesAB_B
    global canvasG, drawLine, img_w, img_h, inA, inB, inC, matchesAC_A, matchesAC_C
    x = event.x
    y = event.y
    
    if x < img_w:
        x2 = x
        y2 = y
        
        ix2 = x
        iy2 = y
        inB = True
        
        canvasG.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, outline="blue",
                         width=2)
        
    elif x > img_w+10 and x < 2*img_w+10:
        x1 = x
        y1 = y
        
        ix1 = x-img_w-10
        iy1 = y
        inA = True
        canvasG.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, outline="yellow",
                         width=2)
    
    elif x> 2*img_w+20:
        x3 = x
        y3 = y
        
        ix3 = x-2*img_w-20
        iy3 = y
        inC = True
        canvasG.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, outline="black",
                         width=2)
    
    if inA == True and inB == True:
        canvasG.create_line(x1, y1, x2, y2, fill="red", width=3)
        matchesAB_A.append([ix1+img_w+10,iy1])
        matchesAB_B.append([ix2,iy2])
        inA = False
        inB = False
        inC = False
        
    elif inC == True and inA == True:
        canvasG.create_line(x1, y1, x3, y3, fill="blue", width=3)
        matchesAC_A.append([ix1,iy1])
        matchesAC_C.append([ix3,iy3])
        inA = False
        inC = False
        inB = False
        
    elif inC == True and inB == True:
        inA = False
        inC = False
        inB = False
        
def loadImage1(image_path):
    global canvasG, img_w, img_h, imageA, imageB, imageALoaded, imageBLoaded
    
    print(image_path.get())
    # Load an image using OpenCV
    cv_img = cv2.cvtColor(cv2.imread(image_path.get()), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.cvtColor(cv2.imread("input_2_1.jpg"), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.imread(image_path.get())
    
    
    cv_img = cv2.resize(cv_img, (img_w, img_h))
    imageB = cv_img
    
    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
    
    # Add a PhotoImage to the Canvas
    canvasG.create_image(0, 0, image=photo, anchor=tk.NW, tags="imageA")
    
    
    if imageBLoaded == True:
        clearSelection()
    
    imageBLoaded = True
    tk.mainloop()
    
def loadImage2(image_path):
    global canvasG, img_w, img_h, imageA, imageB, imageALoaded, imageBLoaded
    
    print(image_path.get())
    # Load an image using OpenCV
    cv_img = cv2.cvtColor(cv2.imread(image_path.get()), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.cvtColor(cv2.imread("input_2_2.jpg"), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.imread(image_path.get())
    
    cv_img = cv2.resize(cv_img, (img_w, img_h))
    imageA= cv_img
    
    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
    
    # Add a PhotoImage to the Canvas
    canvasG.create_image(img_w+10, 0, image=photo, anchor=tk.NW, tags="imageB")
    
    if imageALoaded == True:
        clearSelection()
    
    imageALoaded = True
        
    tk.mainloop()
    
def loadImage3(image_path):
    global canvasG, img_w, img_h, imageA, imageB, imageC, imageALoaded, imageBLoaded, imageCLoaded
    
    print(image_path.get())
    # Load an image using OpenCV
    cv_img = cv2.cvtColor(cv2.imread(image_path.get()), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.cvtColor(cv2.imread("input_2_3.jpg"), cv2.COLOR_BGR2RGB)
    # cv_img = cv2.imread(image_path.get())
    
    cv_img = cv2.resize(cv_img, (img_w, img_h))
    imageC= cv_img
    
    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
    
    # Add a PhotoImage to the Canvas
    canvasG.create_image(2*img_w+20, 0, image=photo, anchor=tk.NW, tags="imageC")
    
    if imageCLoaded == True:
        clearSelection()
    
    imageCLoaded = True
        
    tk.mainloop()
    


def clearSelection():
    global canvasG, img_w, img_h, imageA, imageB, matchesA, matchesB
    global inA,inB,inC
    
    canvasG.delete("all")
    matchesAB_A.clear()
    matchesAB_B.clear()
    
    matchesAC_A.clear()
    matchesAC_C.clear()
    
    inA = inB = inC = False
    
    photoA = ImageTk.PhotoImage(image = Image.fromarray(imageB))
    canvasG.create_image(0, 0, image=photoA, anchor=tk.NW, tags="imageB")
    
    photoB = ImageTk.PhotoImage(image = Image.fromarray(imageA))
    canvasG.create_image(img_w+10, 0, image=photoB, anchor=tk.NW, tags="imageA")
    
    photoC = ImageTk.PhotoImage(image = Image.fromarray(imageC))
    canvasG.create_image(2*img_w+20, 0, image=photoC, anchor=tk.NW, tags="imageC")
    
    tk.mainloop()

def errorPopup(msg):
    popup = tk.Tk()
    popup.wm_title("Error!")
    label = tk.Label(popup, text=msg)
    label.pack(fill='x', padx=50, pady=5)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def matchKeyPoints():
    global matchesA, matchesB, imageA, imageB
    
    if imageALoaded == False or imageBLoaded == False or imageCLoaded == False:
        errorPopup("First select 3 images!")
        return
    
    if len(matchesAB_A) < 4 or len(matchesAC_A) < 4:
        errorPopup("Not Sufficient Points selected\n Select atleast 4 correspondances!")
        return
    
    ptsAB_A = np.float32(matchesAB_A)
    ptsAB_B = np.float32(matchesAB_B)
    
    ptsAC_A = np.float32(matchesAC_A)
    ptsAC_C = np.float32(matchesAC_C)
    
    
    (H_C, status) = cv2.findHomography(ptsAC_C, ptsAC_A, cv2.RANSAC,
				4.0)
    
    (H_B, status) = cv2.findHomography(ptsAB_B, ptsAB_A, cv2.RANSAC,
				4.0)
    
    result = cv2.warpPerspective(imageC, H_C,
			(imageC.shape[1] + imageA.shape[1], imageC.shape[0]))
    
    result[0:imageA.shape[0], 0:imageA.shape[1]] = imageA
    # cv2.imshow("re", result)
    result1 = cv2.warpPerspective(imageB, H_B,
			(imageB.shape[1] + imageA.shape[1]+imageC.shape[1], imageA.shape[0]))
    
    result1[0:imageA.shape[0], imageB.shape[1]:imageB.shape[1]+imageA.shape[1]+imageC.shape[1]] = result
    
    result1 = cv2.cvtColor(result1, cv2.COLOR_RGB2BGR)
    cv2.imshow("Stitched Image", result1)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


#creating main window and widgets
window=tk.Tk() 
  
#getting screen width and height of display 
window_width= window.winfo_screenwidth()  
window_height= window.winfo_screenheight() 

img_w = int((window_width-40)/3) -10
img_h = window_height - 300

#setting tkinter window size 
window.geometry("%dx%d" % (window_width, window_height)) 
window.title("Image Stitching (3 images with center as base) - Kartik Saini") 

# 1st image path input
tk.Label(window, text='First Image Path').grid(row=0, column=0)
img1 = tk.StringVar() 
e1 = tk.Entry(window, textvariable=img1, width=50) 
e1.grid(row=0, column=1)

loadImage1 = partial(loadImage1, img1)  
b1 = tk.Button(window, text='Load', width=10, command=loadImage1)
b1.grid(row=0, column=2)

window.grid_columnconfigure(3, minsize=200)

# 2nd image path input
tk.Label(window, text='Second Image Path').grid(row=0, column=4)
img2 = tk.StringVar() 
e2 = tk.Entry(window, textvariable=img2, width=50) 
e2.grid(row=0, column=5)

loadImage2 = partial(loadImage2, img2)  
b2 = tk.Button(window, text='Load', width=10, command=loadImage2)
b2.grid(row=0, column=6)

# 3rd image path input
tk.Label(window, text='Third Image Path').grid(row=1, column=0)
img3 = tk.StringVar() 
e3 = tk.Entry(window, textvariable=img3, width=50) 
e3.grid(row=1, column=1)

loadImage3 = partial(loadImage3, img3)  
b3 = tk.Button(window, text='Load', width=10, command=loadImage3)
b3.grid(row=1, column=2)

# window.grid_columnconfigure(3, minsize=200)

canvasG = tk.Canvas(window, width=3*img_w+20, height=img_h, bg="grey") 
canvasG.place(x = 10, y=100) 
canvasG.bind("<Button 1>",selectGlobalCanvas)

b4 = tk.Button(window, text='Undo Selection', width=30, command=clearSelection)
b4.place(x=300, y=img_h+120)

# b4 = tk.Button(window, text='Stitch Images', width=30, command=automatch)#matchKeyPoints
b5 = tk.Button(window, text='Stitch Images', width=30, command=matchKeyPoints)
b5.place(x=window_width - 500, y=img_h+120)


window.mainloop() 