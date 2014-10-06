#!/usr/bin/python

import cv2
import os

# 96 * 192
# color

num = 0
while True:
    num += 1
    filename = 'xx1/%s.bmp' % str(num)
    if not os.path.isfile( filename ) :
        break
    print num
    img = cv2.imread(filename)
    #width = len(img[0])
    #height = len(img)
    img =  img[60:]
    #img[:] = [ (lambda x:[ (lambda y:0 if y<160 else 255)(j) for j in x])(i)  for i in gray[:] ]
    #img[:][:][:] = [ i>>4<<4+8 for i in gray[:][:][:] ]
    outname = 'xx1_color/%s.bmp' % str(num)
    cv2.imwrite(outname , img)

