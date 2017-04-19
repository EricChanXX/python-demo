#! /usr/bin/python
# _*_ coding: UTF-8


import time

#获取当前时间
print "获取本地时间"
print "本地时间 :", time.localtime(time.time())
#本地时间戳
print time.time()

print "==========================================="

#格式时间
print "格式化本地时间"
print "本地时间：", time.asctime(time.localtime())

#使用time模块的strftime方法来格式化日期
print "==========================================="
#strftime方法：接收以时间元组，并返回以可读字符串表示的当地时间
print "本地日期:", time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
print "本地日期:", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 

#strptime方法:

str = "Sat Mar 28 22:24:24 2016"

print time.strptime(str,"%a %b %d %H:%M:%S %Y")
#时间戳
print time.mktime(time.strptime(str,"%a %b %d %H:%M:%S %Y"))

#输出日历
import calendar

print "==========================================="
#显示某月的日历
print calendar.month(2017,4)

#判断输入年份是否为闰年
print "是否为闰年：",calendar.isleap(2016)

