# -*- coding:utf-8 -*-

import ntplib
import datetime

client = ntplib.NTPClient()
response = client.request('ntp.aliyun.com')
print(datetime.datetime.fromtimestamp(response.tx_time))
