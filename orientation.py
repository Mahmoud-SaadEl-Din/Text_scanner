import argparse
import cv2
import numpy as np
import imutils

image = cv2.imread('C:\\Users\\mahmo\\Documents\\Image processing\\project\\Captured_images\\original2_thresholded.JPG')
print(type(image))
rotated = imutils.rotate_bound(image, 0)
cv2.imshow("Rotated (Correct)", rotated)
cv2.waitKey(0)