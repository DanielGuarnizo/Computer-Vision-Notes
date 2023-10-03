import cv2 
import numpy as np

# img = cv2.imread("try.png")

# print(f"thw width of the images is: {img.shape[1]}")
# print(f"thw height of the images is: {img.shape[0]}")
# print(f"the number of chanels of the image is: {img.shape[2]}")


# img[0:100,0:100] = (0,0,255)





# cv2.imshow("first ipenCV image", img)
# cv2.waitKey(0)

# cv2.imwrite

canvas = np.zeros((500,500,3), dtype="uint8") # data type generated numbers from 0 - 255
                                            # the shape atribute if the third dimension is not specify 
                                            # it will be a grey scale 


green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)
color =(255,255,255)

# START

cv2.line(canvas, (0,0), (255,255),green, 3)
cv2.line(canvas,(500,0),(255,255),red,3)
cv2.line(canvas,(0,500),(255,255),blue,3)
cv2.line(canvas,(500,500),(255,255),(255,255,0),3)
cv2.rectangle(canvas,(50,50), (200,200), blue, -1) # the last parameter stay by tickness , with -1 we fill the rectangle 


# CIRLCE
centerx, centery, = canvas.shape[1]//2, canvas.shape[0]//2

cv2.circle(canvas, (centerx,centery), 40, color,-1)

#

cv2.imshow("images", canvas)
cv2.waitKey(0)

