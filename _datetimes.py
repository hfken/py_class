#datetime库
from datetime import *
#datetime库下的类
'''
date:日期
time:时间（小时分钟，秒，毫秒）
datetime:表示日期和时间 覆盖date和time
timedelta:有关时间间隔的类
tzinfo:与时区有关的类
'''
d=datetime.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

#创建datetime对象
myday=datetime(2020,11,10,1,2,2,123456)
print(myday.microsecond)

#datetime对象格式化
print(myday.strftime('%Y年%m月%d日'))#2020年11月10日


#strptime()则执行相反操作，将字符串转成datetime对象
date_str = "2023-01-15 14:30:45"
format_str = "%Y-%m-%d %H:%M:%S" #要对照写好
dt_obj = datetime.strptime(date_str, format_str)
print(dt_obj)       # 输出: 2023-01-15 14:30:45
print(type(dt_obj)) # 输出: <class 'datetime.datetime'>

#isoformat和isoweekday函数
#isoformat采用ISO标准显示时间
#isoweekday计算datetime是星期几