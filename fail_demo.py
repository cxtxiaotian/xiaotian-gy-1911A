#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1,读写文件操作
#写入
#绝对路径写入
#写入W 先清空文件 后写入内容。a往文件的末尾追加内容.b把文件原封不动的
#写入文件，一般用于上传文件。
#encoding="utf-8" 解决文件写入中文时乱码问题。writelines([ \n ])写入列表\n是换行
# ？
#读取文件
# f=open("test1.txt","r",encoding="utf-8")
#c=f.read()
#print(c)
#f.close()
#按行读取文件全部内容
#lines=f.readlines()
#print(lines)
#读取一行内容
# line=f.readline()
# print(line)
# f.close()
#with是一个上下文管理器，with内的代码在执行结束或者是执行出错的时候
#都会自动执行释放系统资源的操作
# with open("test1.txt","r",encoding="utf-8")as f:
#     c=f.read()
#     print(c)
#类 相当于一个模板，没有实体
# class ClassA1():
#     a1=10
#     def print_a(self):
#         print(self.a1)
# #类的实例化
# c=ClassA1()
# c.print_a()
class produt():
    size="6寸"
    def __init__(self,color):
        self.color=color

    def call(self):
        print("hello")
#实例化
phone1=produt("土豪金")
#获取属性
print(phone1.color)
print(phone1.size)
#调用方法
phone1.call()

from product import product1
phone1=product1()