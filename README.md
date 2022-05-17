# Edge-Detection
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import the necessary modules.

### Step 2:
Convert the BGR image to gray scale image 

### Step3:
For performing edge detection on a image. Use the following operators on the image:

Sobel
```python
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,5)
sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,5)
```

Laplacian

```python
Laplacian=cv2.Laplacian(img,cv2.CV_64F)
```
Canny
```python
canny=cv2.Canny(img,120,150)
```


## Program:

``` Python
# Import the packages
import cv2
import matplotlib.pyplot as plt
from cv2 import COLOR_BGR2GRAY
```

# Load the image, Convert to grayscale and remove noise
```python 
image=cv2.imread("tata.jpg")
gray=cv2.cvtColor(image,COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray,(3,3),0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobelxy =cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

```
# SOBEL EDGE DETECTOR
```python

plt.subplot(2,2,2)
plt.imshow(sobelx)
plt.title('sobelx')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobely)
plt.title('sobely')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobelxy)
plt.title('sobelxy')
plt.xticks([]), plt.yticks([])
plt.show()
```

# LAPLACIAN EDGE DETECTOR

```python 

# cv2.waitKey(0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.imshow(laplacian)
plt.title('laplacian')
plt.show()

```

# CANNY EDGE DETECTOR

```python
canny_edges = cv2.Canny(img, 120, 150)
plt.imshow(canny_edges)
plt.title('canny_edges')
plt.show()


```
## Output:
### SOBEL EDGE DETECTOR
<br>

![Screenshot (2)](https://user-images.githubusercontent.com/75234646/168790422-ee53a35b-49e3-48df-a6f5-99ea39d51258.png)

<br>


### LAPLACIAN EDGE DETECTOR
<br>

![Screenshot (6)](https://user-images.githubusercontent.com/75234646/168790916-a9d5dd58-a39e-4f41-a7bd-21e67ad92b14.png)


<br>


### CANNY EDGE DETECTOR
<br>

![Screenshot (5)](https://user-images.githubusercontent.com/75234646/168791172-0c047684-6a61-4ee3-9f75-46c4695785b0.png)

<br>

## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
