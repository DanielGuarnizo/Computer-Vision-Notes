import math
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/cube_try.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# def onClick(event, x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if len(dst_points) < 4:
#             dst_points.append([x,y])
#             cv2.circle(img_copy,(x,y), 50 ,(0,0,255), -1)
#             cv2.imshow("Base img", img_copy)

# source points
def onClick(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(src_points) < 4:
            src_points.append([x,y])
            cv2.circle(img,(x,y), 50 ,(0,0,255), -1)
            cv2.imshow("Base img", img)

# create source and destination point 
src_points = []

cv2.namedWindow("Base img", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Base img",onClick)
cv2.imshow("Base img", img)
cv2.waitKey(0)

d = math.dist(src_points[0], src_points[1])
# print(src_points, d)
d = int(d)
dst_points = np.array([[10,10],[10,d+ 10],[d +10,d + 10],[d+10,10]], dtype=np.float32)
src_points = np.array(src_points, dtype=np.float32)
H = cv2.getPerspectiveTransform(src_points, dst_points) 
warped = cv2.warpPerspective(img,H,(d+10, d+ 10))
cv2.imshow("try", warped)