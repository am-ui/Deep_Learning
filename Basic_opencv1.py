#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import the importatnt library
import cv2
import skimage
from skimage.measure import compare_ssim
import imutils
import argparse
#read the image
imageA = cv2.imread(r"C:\Users\AMIT\Downloads\nature_pic.jpg")
#Resize the image
imageA.resize(imageA, (450, 320))
imageB = cv2.imread(r"C:\Users\AMIT\cat_pic.jpg")
imageB.resize(imageB, (450,320))
#plot the images
cv2.imshow("orignal_image", imageA)
cv2.imshow("cat_image", imageB)
#convert BRG color to GRAY color
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2,cvtColor(imageB, cv2.COLOR_BRG2GRAY)
#compare the two images
comp = compare_ssim(grayA, grayB)
comp.resize(comp, (920,450))
cv2.imshow("compared images", comp)
cv2.waitKey(0)
cv2.destroyAllWindow()


# In[ ]:




