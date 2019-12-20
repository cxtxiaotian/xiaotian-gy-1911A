#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
try:
    os.mkdir("gy_B")
except FileExistsError:
    print("文件夹已存在")
else:
    print("文件夹创建成功")
finally:
    print("创建文件夹")


