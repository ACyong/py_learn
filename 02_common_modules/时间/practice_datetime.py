import datetime

# 1.字符串转日期
detester = '2022-10-01'
date = datetime.datetime.strptime(detester, '%Y-%m-%d')
print(date)

# 2.日期转字符串
date = datetime.datetime.now()
print(date)
detester = date.strftime('%Y-%m-%d %H:%M:%S')
print(detester)
