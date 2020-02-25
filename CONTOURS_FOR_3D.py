import sys
import numpy as np
import cv2

hsv_min = np.array((100, 100, 100), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

img = cv2.imread('/home/tim/contur.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gabarits = np.ma.shape(img)
white_picture = np.zeros((gabarits[0],gabarits[1], gabarits[2]), np.uint8)
color = tuple(reversed((255,255,255)))
# Fill image with color
white_picture[:] = color

print(gabarits)

ret, thresh = cv2.threshold(gray, 120, 255, 0)
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(white_picture, contours, -1, (0, 255, 0), 1)
cv2.imshow('contours', white_picture)

key = cv2.waitKeyEx()

cv2.destroyAllWindows()
