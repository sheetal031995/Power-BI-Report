'''
datetime module: Related to date and time.


datetime module contains datetime and date object.

      datetime
         |
    ----------
   |          |    
  datetime    date
               |
               -year
               -month   => datetime.date.month
               -day
'''
'''
import datetime as dt

print("minimum year:",dt.MINYEAR)
print("maximum year:",dt.MAXYEAR)

x=dt.date(2022,5,15)
print(type(x))
print(x)

print("year:",x.year) #x=dt.date()=>datetime.date()
print("month:",x.month)
print("day:",x.day)

'''
'''
#to get the system date

from datetime import date

d=date.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

'''
'''
import datetime as dt

x=dt.datetime(2021,9,9,11,40,30,5000)
print(type(x))
print(x)

print("year:",x.year)
print("month:",x.month)
print("day:",x.day)

print("hour:",x.hour)
print("minute:",x.minute)
print("second:",x.second)

'''

from datetime import datetime

dt=datetime.today()
print(dt)




