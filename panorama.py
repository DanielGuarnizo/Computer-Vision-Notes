import numpy as np
import cv2
# load the image for building the panorama
left = cv2.imread("images/left.png")
right = cv2.imread("images/right.png")

# create an instance of the ORB
orb = cv2.ORB_create() # the dtype of the descriptors given the ORB algorithm are binary numbers 

# compute the features of the both images 
kpts1, des1 = orb.detectAndCompute(left, None)
kpts2, des2 = orb.detectAndCompute(right, None)

# we match the keypoints through knn, is a clasification algorithm: having some points in the plain and  new point appears
# then the new point will be assign to a new class w.r.t the nearest clustter the that point , this is taking from the distance of that point oìto the clas
matcher = cv2.BFMatcher(cv2.NORM_HAMMING) # intance from the matcher alfìgorithm 
matches = matcher.knnMatch(des1, des2 ,k=2)
print(matches)
# 
good_matches = []
for m,n in matches:
    if m.distance < 0.03 * n.distance: # m.distance are distance between point in the matches in this case just 2 
        good_matches.append(m)

# check if we have at least 4 points for omputing the homography 
if len(good_matches) >= 4:
    src_points = np.float32([kpts1[m.queryIdx].pt for m in good_matches])
    dst_points = np.float32([kpts2[m.trainIdx].pt for m in good_matches])

    M,mask = cv2.findHomography(src_points,dst_points, cv2.RANSAC, 5.0)
        # difference between warp prospetive is that this fucntion use an algorithm to map the points , is the poitn
        # to match is between the range of 5.0 pixel then that point will be accepted otherwise discarted 

    # transform the image and stirch it with the other 

    dst = cv2.warpPerspective(left, M,(left.shape[1] + right.shape[1], left.shape[0])) # (width, height)
    dst[0:right.shape[0],0: right.shape[1]] = right.copy()




    cv2.imshow("panorama",dst)
    cv2.waitKey(0)