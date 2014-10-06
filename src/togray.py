#!/usr/bin/python

import cv2
import os

num = 0
while True:
    num += 1
    filename = 'xx1/%s.bmp' % str(num)
    if not os.path.isfile( filename ) :
        break
    print num
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,6)
    #width = len(img[0])
    #height = len(img)
    gray =  gray[60:]
    gray[:] = [ (lambda x:[ (lambda y:0 if y<160 else 255)(j) for j in x])(i)  for i in gray[:] ]
    outname = 'xx1_bin/%s.bmp' % str(num)
    cv2.imwrite(outname , gray)
