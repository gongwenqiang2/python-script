# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'




from pytesser import *
im = Image.open(r'C:\software\data\python\Lib\site-packages\pytesser\fnord.tif')
textcode = image_to_string(im)
print textcode