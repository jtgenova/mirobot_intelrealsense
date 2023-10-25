import os
import cv2
import numpy as np

image_path = "images/rgb.jpeg"
# segment rgb image
color_image = cv2.imread(image_path)

hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
# Define the lower and upper bounds of the blueish color in HSV
lower_red = np.array([0,190,100])   # Lower bounds for redish color
upper_red = np.array([15,255,255]) # Upper bounds for redish color
# Create a mask that selects the blueish color in the image
mask = cv2.inRange(hsv_image, lower_red, upper_red)
mask_path = "temp_mask.jpeg"
cv2.imwrite(mask_path, mask)