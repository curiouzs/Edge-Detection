# Import the packages
import cv2
import matplotlib.pyplot as plt
from cv2 import COLOR_BGR2GRAY
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

# cv2.waitKey(0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.imshow(laplacian)
plt.title('laplacian')
plt.show()
canny_edges = cv2.Canny(img, 120, 150)
plt.imshow(canny_edges)
plt.title('canny_edges')
plt.show()
