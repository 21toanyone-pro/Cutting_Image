# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:32:44 2019

@author: Lim
"""
from PIL import Image, ImageFilter
from PIL import ImageFont 
from PIL import ImageDraw 
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import glob

file_path = './image/a/'
bground_list = os.listdir(file_path)
count = len(bground_list)



file_path2 = './resize/a/'
bground_list2 = os.listdir(file_path2)

for j in range(count):
        src = cv2.imread(file_path+str(bground_list[j]), cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
        ret, dst = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

        dir_path = './resize/a/'

        if not os.path.isdir(dir_path):
                        os.mkdir(dir_path) 

        fname = str(j) + '.jpg'
        cv2.imwrite(dir_path + fname, dst)


        img = Image.open(file_path2+str(bground_list2[j]))
        re = img.resize((540, 960))
        area = (10, 98, 505, 880)
        cropped_img = re.crop(area)

        dir_path2 = './resize/cut/'
        
        if not os.path.isdir(dir_path2):
                os.mkdir(dir_path2 + '/')  
        
        cropped_img.save(dir_path2 + fname)


#cropped_img.save('./resize/a/' + '01' + '.jpg')



#자를 크기 위로 98 아래에서 79
#오른쪽에서 32


