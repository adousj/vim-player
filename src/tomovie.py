#!/usr/bin/python

import aalib
import Image
import os

columnnum = 100
linenum = 30 
timenum = 40 

screen = aalib.AsciiScreen( width=columnnum,height=linenum )


'''
out = open('xx1_bin.txt','w')
i = 0
while True:
    i += 1
    filename = 'xx1_bin/%s.bmp' % str(i)
    if not os.path.isfile(filename) :
        break 
    print i
    image = Image.open(filename).convert('L').resize(screen.virtual_size)
    screen.put_image((0,0),image)
    out.write(screen.render())
    out.write('\n')

'''

out = open('xx1_color.txt','w')
i = 0
while True:
    i += 1
    filename = 'xx1_color/%s.bmp' % str(i)
    if not os.path.isfile(filename) :
        break 
    print i
    image = Image.open(filename).convert('L').resize(screen.virtual_size)
    screen.put_image((0,0),image)
    out.write(screen.render())
    out.write('\n')

out.write('\nframe %d  line %d   column %d   time %d' % ( i-1 , linenum , columnnum , timenum ) )
out.close()

