
# datetime kullanımı

from datetime import date

bugun=date.today()
print(bugun)

dun=date(2021, 2, 7)
print(dun)

print(bugun-dun)
print((bugun-dun).days)
print(bugun.month)

print(date.isocalendar(bugun))
print(date.weekday(bugun))
print(date.ctime(bugun))

from datetime import time

zaman=time(21,15,25)
print(zaman)
print(zaman.hour)

import datetime
zaman2=datetime.datetime(2021,2,8,20,13,47)
print(zaman2)