#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100 #赋值整型变量
miles = 1000.0 #浮点型
name = "Jason" #字符型

a , b , c = 1 , 2, "abc"

print counter
print miles
print name

print a
print b
print c

#python 五种标准 数据类型
#number (数字)，string（字符串），list(列表)，tuple（元组）,dictionary(字典)

#数字number，4种基本类型 int(有符号整形) long（长整形） float（浮点型） complex（复数）
a = 15.0
b = complex(a,b)
print a
print b

#字符串string
str = "My name is Jason Chen,oranges is my favorite!!!"

print str
print str[1]
print str[3:7]
print str*2

#列表list,可以二次赋值，复合数据结构，元素可以是数字和字符
list = ['My' , 'name' , 'is' , 'Jason' , 'Chen']
list1 = ['oranges' , 'is' , 'my' , 'favorite!!!']
print list
list[1] = 'NAME'
print list[1]
print list
print list[3:7]
print list +list1

#元组tuple 类似于列表list ，但是使用小括号（），赋值变量，且后边赋值不能更改
#元组相当于只读列表。
tu = ('My' , 'favorite' , 'is' , 'Oranges')

print tu

#字典dictionary 
#列表是有序的对象结合，字典是无序的对象集合。
#两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典使用花括号{}，字典由索引(key)和它对应的值value组成。

dic = {}
dic['v1'] = "hello world!"
dic [1] = "welcome to python world!"

dic1 = {'lastName': 'JSON' , 'firstName': 'CHEN'}

print dic1['lastName']
print dic[1]
print dic1.values()

