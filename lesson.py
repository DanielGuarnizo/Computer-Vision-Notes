
import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread("images/flower.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray_img)

cv2.imshow("original", gray_img)
cv2.imshow("equalized", equalized)
cv2.waitKey(0)

# plt.plot(hist)
# plt.xlim([0,255])
# plt.show()