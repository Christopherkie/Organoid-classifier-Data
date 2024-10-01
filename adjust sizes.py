# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:39:16 2024

@author: chris
"""

from PIL import Image 
import numpy as np
import os.path
import os

  
# Opening the primary image (used in background) 

  



directory=os.fsencode('D:/16992_add')
for file in os.listdir(directory):
    img1 = Image.open('C:/Users/chris/OneDrive/Desktop/backgroundimage.jpg')
    filename = os.fsdecode(file)
    filename=os.path.join('D:/16992_add', filename)
    img2 = Image.open(filename)
    sizex=img2.size[0]
    sizey=img2.size[1]
    
    
    startx=int(np.floor((650-sizex)/2))
    starty=int(np.floor((602-sizey)/2))
    img1.paste(img2,(startx,starty)) 
      
    # Displaying the image 
    #img1.show()
    img1=img1.save(filename, format='jpeg')