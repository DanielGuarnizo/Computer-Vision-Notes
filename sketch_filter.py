# import cv2 
# import numpy as np

# # load the image to cartoonize
# img = cv2.imread("images/girl.png")

# # convert the image to grayscale 
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # apply median blur to remove niose 
# img_gray = cv2.medianBlur(img_gray,5) #! how is used the kernel size in this function 

# # extract the edges with Laplacian #! why 
# # the countour of the figures inside the image 
# edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)

# # thresholding  the edges 
# #? this function take a pixel or color it the value is below the threshold the it will set it's value to black
# #? if the value is above the threshold the the color is set to white 

# _, thresholded = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)

# # get the color with the bilateral filter 
# color_img = cv2.bilateralFilter(img,10,250,250) # img, kernel , sigma_x , sigma_y, this function use a 
#                                                 # gaussian distribution 

# # merge color and edges 
# skt = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)
# sketch_img = cv2.bitwise_and(color_img, skt)

# cv2.namedWindow("Image", cv2.WINDOW_KEEPRATIO)
# cv2.imshow("Image",sketch_img)

import cv2
import numpy as np

#load the image to CARTOONIZE 

img = cv2.imread("images/girl.png")

# convert the image to grayscale 
img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# apply median blur to remove noise 
img_gray= cv2.medianBlur(img_gray,5)

#extract the edges with Laplacian
edges= cv2.Laplacian(img_gray,cv2.CV_8U, ksize=5)

# thresholding the edges 

_, thresholded= cv2.threshold(edges,70,255, cv2.THRESH_BINARY_INV)

#get the colors with the bilateral filter 
color_img= cv2.bilateralFilter(img, 10,250,250)

#merge color and edges
skt= cv2.cvtColor(thresholded,cv2.COLOR_GRAY2BGR)
sketch_img= cv2.bitwise_and(color_img,skt)

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.imshow('img', sketch_img)

cv2.waitKey(0)
