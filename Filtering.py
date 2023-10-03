import numpy as np 
import cv2 

x = np.uint8([250])
y = np.uint([50])

result_opencv = cv2.add(x,y)
result_numpy = x + y 
