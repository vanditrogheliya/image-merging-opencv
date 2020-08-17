import cv2
import numpy as np
apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

apple_copy = apple.copy()
gp_apple = [apple_copy]
orange_copy = orange.copy()
gp_orange = [orange_copy]


for i in range (2):
    apple_copy = cv2.pyrDown(apple)
    gp_apple.append(apple_copy)

    orange = cv2.pyrDown(orange)
    gp_orange.append(orange_copy)

apple_copy = gp_apple[1]
lp_apple = [apple_copy]
orange_copy = gp_orange[1]
lp_orange = [orange_copy]

for i in range (1,0,-1):
    gaussian_exapnded = cv2.pyrUp(gp_apple)
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_exapnded)
    lp_apple.append(laplacian)

    gaussian_exapnded = cv2.pyrUp(gp_orange)
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_exapnded)
    lp_orange.append(laplacian)
    orange = cv2.pyrUp(orange)




cv2.imshow('mix', mix)
cv2.waitKey(0)
