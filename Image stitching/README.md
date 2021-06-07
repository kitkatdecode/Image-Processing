This python based tool is used to stich 2 or 3 images by manually selecting matching points in corresponding images. It uses homography transformation to stitch images.


Result will depend on number of points matched and quality of matching. At least 4 matches required to compute homography.

Selection can be cleared using **Undo Selection**.

Libraries used-

- opencv
- tkinter
- Pillow

run cmd - 

```
$ python3 stich2images.py

$ python3 sticth3images.py
```

Using the tool-
-	There are entry fields provided to load images using image file path
-	After opening the images, select one point from one image and second from other adjacent image to select corresponding matching points.
-	At least 4 correspondance points must be selected
-	Selected points can be undone
-	Selecting multiple points in same image simulataneously will consider last point selected for matching
-	Output image will be shown in separate window


Results-

stich2images.py

2 images example-

![alt text](https://github.com/kaySource/Image-Processing/blob/main/Image%20stitching/results/2images.png)

Result

![alt text](https://github.com/kaySource/Image-Processing/blob/main/Image%20stitching/results/2imagesResult.png)

3 images example-

![alt text](https://github.com/kaySource/Image-Processing/blob/main/Image%20stitching/results/3images.png)

Result

![alt text](https://github.com/kaySource/Image-Processing/blob/main/Image%20stitching/results/3imagesResult.png)
