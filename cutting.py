# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:32:44 2019

@author: Lim
"""
from PIL import Image, ImageFilter
from PIL import ImageFont 
from PIL import ImageDraw 
import cv2
import numpy as np
import os
import glob

file_path = './image/a/'
bground_list = os.listdir(file_path)
count = len(bground_list)

for j in range(count):
    img = Image.open(file_path+str(bground_list[j]))
    re = img.resize((540, 960))
    area = (10, 98, 505, 880)
    cropped_img = re.crop(area)
    
    s_name = str(j)
    cropped_img.save('./resize/a/' + s_name + '.jpg')
    (img_h, img_w) = cropped_img.size    
    grid_w = 33 # crop width
    grid_h = img_h # crop height
    range_w = (int)(img_w/grid_w)
    dir_path = './resize/a/' + str(j) +'/'

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path + '/')    


    i = 0
    for w in range(15):
        bbox = (w*33,0,(w+1)*33,782)
        # 가로 세로 시작, 가로 세로 끝
        crop_img = cropped_img.crop(bbox)

        fname = str(i) + '.jpg'
        savename = dir_path + fname
        crop_img.save(dir_path + fname)
        i += 1

    


#cropped_img.save('./resize/a/' + '01' + '.jpg')



#자를 크기 위로 98 아래에서 79
#오른쪽에서 32


