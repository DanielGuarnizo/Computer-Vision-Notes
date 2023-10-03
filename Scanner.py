import cv2
import numpy as np 

# callback definition 
def onClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(src_points) < 4:
            src_points.append([x,y])
            cv2.circle(img_copy,(x,y), 10 ,(0,0,255), -1)
            cv2.imshow("Img", img_copy)



img = cv2.imread("images/gerry.png")
img_copy = img.copy()

# create the satriting points set 

src_points = []


# src_points = np.array([
#             [28,277],
#             [131,987],
#             [730,860],
#             [572,149]
# ], dtype = np.float32) # passing integers number will rease an error 

            #? the array have the points in a counter wise order , starting from the top left and 
            #? ending at the top right corner 



# create the destination points 

dst_points = np.array([
            [0,0],
            [0,800],
            [600,800],
            [600,0]
], dtype = np.float32) # [colums, row]

# show the images to getting the corners                     
cv2.namedWindow("Img", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Img", onClick)  # assoaciated the onClick function to  our window to get the corners 

cv2.imshow("Img", img_copy)
cv2.waitKey(0)

# compute the homography matrix 
#? it will be the transformation matrix we will applied to the original image 
src_float = np.array(src_points, dtype= np.float32) #create a numby array passing as argument a list of python 
H = cv2.getPerspectiveTransform(src_float, dst_points)


# apply to original img
output_img = cv2.warpPerspective(img, H,(600,800))


#create the window 
cv2.namedWindow("Output", cv2.WINDOW_KEEPRATIO)

cv2.imshow("Img", img)
cv2.imshow("Output", output_img)
cv2.waitKey(0)