import cv2
import numpy as np

# Load the images
img1 = cv2.imread('E:/BE_PROJECTNO_9/latest_tpgan/dataset/front_face/219/219_01_01_140_06_cropped.jpg')
img2 = cv2.imread('E:/BE_PROJECTNO_9/latest_tpgan/generated_image.jpg')

# Compute the Euclidean distance between the images
distance = np.linalg.norm(img1 - img2)

print("The Euclidean distance between the images is: {}".format(distance))