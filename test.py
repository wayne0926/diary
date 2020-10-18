import requests
playload = {'key': '91feef17aa2cd875a61f7520dd30207a'}
pl = requests.get('https://restapi.amap.com/v3/ip', params=playload)
re = pl.json()['adcode']
print(re)
playload1 = {'city': re, 'key': '91feef17aa2cd875a61f7520dd30207a', 'extensions': 'base'}
we = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=playload1)
# print(we.json())
rew = we.json()['lives'][0]['city']
weas = we.json()['lives'][0]['weather']
print(rew)
print(weas)
