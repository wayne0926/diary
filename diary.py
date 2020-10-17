#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者：魏然
# 更新：2020/10/17
# 引入模块
import time
# 定义系统时间变量
time = time.strftime("%Y年%m月%d日 %H:%M", time.localtime())
# 询问名字
name = input('鼎鼎大名：')
# 询问天气
weather = input('天气如何？')
# 询问地点
place = input('我在：')
# 询问时间
thing = input('做了啥事？')
# 询问心情
mood = input('心情如何？')
# 汇总所有内容
out = '>>>> ' + time + '   ' + place + '   ' + weather + ' <<<<' + '\n' + thing + '，' + '感觉' + mood + '\n' + '\n     >>>' + name + '<<<' + '\n'
# 新建(打开)文件
f = open('diary.txt', mode='a')
# 写入(追加)文件
f.write(out)
# 关闭文件
f.close
# 打印结果
print(out)
