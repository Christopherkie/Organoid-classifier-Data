# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:42:56 2024

@author: chris
"""

from PIL import Image
import os.path
import os

counter=0
minx=1000
miny=1000
directory=os.fsencode('D:/16992_add')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename=os.path.join('D:/16992_add', filename)
    img = Image.open(filename)
    if img.size[0]<=minx:
        minx=img.size[0]
    if img.size[1]<=miny:
        miny=img.size[1]
    #print(os.fsdecode(file))
    #print(img.size)
    if not img.size==(650,602):
        counter+=1
        
print(counter, minx, miny)