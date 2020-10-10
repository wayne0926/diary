#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
time1 = time.strftime("%Y年%m月%d日 %H:%M", time.localtime()) 
# time = input('什么时间？')
name = input('鼎鼎大名：')
weather = input('天气如何？')
place = input('我在：')
thing = input('做了啥事？')
mood = input('心情如何？')
out = '>>>> ' + time1 + '   ' + place + '   ' + weather + ' <<<<' + '\n'  + thing + '，' + '感觉' + mood + '\n' + '\n     >>>' + name + '<<<' + '\n'
f = open('123.txt',mode='a')
f.write(out)
f.close
print(out)
