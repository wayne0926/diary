#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者：魏然
# 更新：2020/10/17 22：26
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
out = '===== ' + time + '   ' + place + '   ' + weather + ' =====' + '\n' + thing + '，' + '感觉' + mood + '\n' + '\n     ===>' + name + '<===' + '\n'
# 将所有信息汇入表
oul = [time, place, name, thing, mood]
# 依次打印(列表)
print('==============================')
print('时间：' + oul[0])
print('------------------------------')
print('地点：' + oul[1])
print('------------------------------')
print('人物：' + oul[2])
print('------------------------------')
print('事件：' + oul[3])
print('------------------------------')
print('心情：' + oul[4])
print('==============================')
# 新建(打开)文件
f = open('diary.txt', mode='a')
# 写入(追加)文件
f.write(out)
# 关闭文件
f.close
# 打印结果(输出)
print(out)
# 显示完成提示语
print("\033[1m完成：" + "已将文本输出在程序目录下的diary.txt")
# 等待用户输入
e = input('=============>回车退出<=============')
# 判断并退出
if e == '':
    exit
