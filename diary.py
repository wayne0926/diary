#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者：魏然
# 更新：2021/7/9
# 注意！：“丨”是中文里的“shù”
# 引入模块
import time
import sys
import os
import datetime
import requests
import ntplib
import codecs
# 位置，天气，时间赋值
# 设置高德API秘钥
p = {'key': '91feef17aa2cd875a61f7520dd30207a'}
# 获取API返回的JSON并取回“status”（是否成功（值为0或1,0表示失败；1表示成功）），然后赋值给“t”
t = requests.get('https://restapi.amap.com/v3/ip', params=p).json()['status']
# 判断t是否不等于“1”（不成功）
if t != '1':
    # 向后传递失败信息（“0”）
    t = '0'
# 若“t”不是“1”（不成功）
else:
    # GET获取API返回的JSON并取回“adcode”（高德位置编码），然后赋值给“pCode”
    pCode = requests.get('https://restapi.amap.com/v3/ip',
                         params=p).json()['adcode']
# 判断是否成功（是否为“1”），若不成功（不等于“1”）
if t != '1':
    # 手动输入信息（天气+位置）
    place = input('天气：')
    wea = input('位置：')
# 如果“t”等于“1”（成功）
else:
    # 设置高德API秘钥以及位置编码
    p = {'city': pCode, 'key': '91feef17aa2cd875a61f7520dd30207a', 'extensions': 'base'}
    # GET获取API返回的JSON并取回“city”（城市），然后赋值给“place”
    place = requests.get(
        'https://restapi.amap.com/v3/weather/weatherInfo', params=p).json()['lives'][0]['city']
    # GET获取API返回的JSON并取回“weather”（天气（中文提示）），然后赋值给“we”
    we = requests.get('https://restapi.amap.com/v3/weather/weatherInfo',
                      params=p).json()['lives'][0]['weather']
    # GET获取API返回的JSON并取回“temperature”（温度），然后赋值给“tem”
    tem = requests.get('https://restapi.amap.com/v3/weather/weatherInfo',
                       params=p).json()['lives'][0]['temperature'] + '℃'
    # 汇总天气（中文提示）与温度，并赋值给“wea”
    wea = we + '丨' + tem

# 获取系统时间然后赋值给“time”
# time = time.strftime("%Y年%m月%d日丨%A丨%H:%M", time.localtime())
# 设置获取方式（NTP）
client = ntplib.NTPClient()
# 获取时间值
response = client.request('ntp.aliyun.com')
# 格式化时间戳
qqq = datetime.datetime.fromtimestamp(response.tx_time)
# 进一步格式化
time = qqq.strftime("%Y年%m月%d日丨%A丨%H:%M")

# 询问名字
name = input('鼎鼎大名：')
# 询问时间
thing = input('做了啥事？')
# 询问心情
mood = input('心情如何？')
# 汇总所有内容
out = '===== ' + time + '丨' + place + '丨' + wea + ' =====' + '\n' + \
    thing + '，' + '感觉' + mood + '\n' + '\n    ===>' + name + '<===' + '\n\n'
# 将所有信息汇入表
oul = [time, place, name, thing, wea, mood]
# 依次打印(列表)
print('======================================================================')
print('时间：' + oul[0])
print('----------------------------------------------------------------------')
print('地点：' + oul[1])
print('----------------------------------------------------------------------')
print('人物：' + oul[2])
print('----------------------------------------------------------------------')
print('事件：' + oul[3])
print('----------------------------------------------------------------------')
print('天气：' + oul[4])
print('----------------------------------------------------------------------')
print('心情：' + oul[5])
print('======================================================================')
# 新建(打开)文件
f = codecs.open('diary.txt', mode='a', encoding='utf-8')
# 写入(追加)文件
f.write(out)
# 打印结果(输出)
print(out)
# 显示完成提示语
print("\033[1m完成：" + "已将文本输出在程序目录下的diary.txt")
# 等待用户输入
e = input('=============>回车保存退出<=============')
# 判断并退出
if e == '':
    sys.exit()
