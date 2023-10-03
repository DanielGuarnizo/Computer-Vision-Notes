import cv2
import numpy as np

#load the image to CARTOONIZE 
'''
img= cv2.imread('gerry.png')

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
'''


#video capture 
cap= cv2.VideoCapture(0)

while True :
    # read the current frame 
    img= cap.read()[1]   # the read function will return a feedback boolean value and the proper image 

    # convert the image to grayscale 
    #img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


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
    k=cv2.waitKey(10)
    if k == ord('q'):
        break
    


