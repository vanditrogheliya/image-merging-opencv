import cv2
import numpy as np
apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

mix = np.hstack((apple[:,180:200], orange[:,135:150]))

for i in range (3):
    mix = cv2.pyrDown(mix)

for i in range (3):
    mix = cv2.pyrUp(mix)

apple_orange1 = np.hstack((apple[:,:179],mix[:,:] ))
apple_orange = np.hstack((apple_orange1[:,:],orange[:,151:] ))

for i in range (1):
    apple_orange = cv2.pyrDown(apple_orange)

for i in range (1):
    apple_orange = cv2.pyrUp(apple_orange)


cv2.imshow('apple-orange', apple_orange[50:300,50:300])

cv2.waitKey(0)
