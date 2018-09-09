#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/8 17:47
import tesserocr
import os
from PIL import Image
image = Image.open(os.getcwd()+'\\'+'1.png')
result = tesserocr.image_to_text(image)
print(result)