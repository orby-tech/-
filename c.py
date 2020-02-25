import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import scipy.misc
from skimage import feature
from PIL import Image
import sys
import cv2

# параметры цветового фильтра
hsv_min = np.array((0,0,0), np.uint8)
hsv_max = np.array((200, 255, 255), np.uint8)


cam = cv2.VideoCapture(0)
while True:
    s, img = cam.read()
    gray =  cv2.cvtColor( img,  cv2.COLOR_BGR2GRAY)

    gray =  feature.canny(gray,  sigma= 1 )
    gray = np.asarray( gray, dtype="int64" )
    cv2.imshow('contours', gray) # выводим итоговое изображение в окно

    key = cv2.waitKey(10)
    if key==ord('1'):
        print("dd")
        break
    
cv2.destroyAllWindows()