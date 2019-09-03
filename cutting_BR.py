# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image, ImageFilter
from PIL import ImageFont 
from PIL import ImageDraw 
import cv2
import numpy as np
import os
import glob

file_path = './image/a/01a.jpg'

src = cv2.imread(file_path, cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

re = 