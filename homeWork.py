import cv2 
import numpy as np 

def onClick(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(dst_points) < 4:
            dst_points.append([x,y])
            cv2.circle(img_copy,(x,y), 50 ,(0,0,255), -1)
            cv2.imshow("Base img", img_copy)

# load images
base_img = cv2.imread("images/billboard.png")
img2 = cv2.imread("images/pablo.png")
img_copy = base_img.copy()

# get image data
base_h, base_w = base_img.shape[:2]
img2_h, img2_w = img2.shape[:2]

# create source and destination points sets 
src_points = np.array([[0,0],[0,img2_h],[img2_w, img2_h],[img2_w,0]], dtype=np.float32) # are the cornes of the images we wanna attach 
dst_points = []


cv2.namedWindow("Base img", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Base img",onClick)
cv2.imshow("Base img", img_copy)
cv2.waitKey(0)


# computing the homography matrix 
dst_points = np.array(dst_points, dtype=np.float32)
H = cv2.getPerspectiveTransform(src_points, dst_points) 

# apply H to the image to be warped
warped = cv2.warpPerspective(img2,H,(base_w, base_h))
cv2.imshow("warped img", warped)
cv2.waitKey(0)

# create the mask 
mask = np.zeros(base_img.shape,dtype=np.uint8)
cv2.imshow("mask", mask)
cv2.waitKey(0)


#set to white the pixels that we want to copy in the billboard 
cv2.fillConvexPoly(mask,np.int32([dst_points]),(255,255,255))
cv2.imshow("mask_fill", mask)
cv2.waitKey(0)

# invert the mask 
mask = cv2.bitwise_not(mask)
cv2.imshow("mask_invert", mask)
cv2.waitKey(0)

# apply the mask to the billboard image
masked_bill = cv2.bitwise_and(base_img,mask)
cv2.imshow("masked bill", masked_bill)
cv2.waitKey(0)

# apply the mask to the warped image
final_img = cv2.bitwise_or(masked_bill,warped)



cv2.namedWindow("Img 2", cv2.WINDOW_KEEPRATIO)
cv2.imshow("Img 2",final_img)
cv2.waitKey(0)