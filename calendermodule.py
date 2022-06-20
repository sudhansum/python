from datetime import *
import calendar as cl

# yer = int(input("enter the year"))
# mth = int(input("enter the  month"))
# dy = int(input("enter the  day"))
#
# c = date(yer, mth, dy)
# print(c)
#
# e = date.today()
# print(e)
#
# g = (e - c).days / 365
# print(g, "years")

x = date.today()
print("current date is ", x)
print(x.year)
print(x.month)
print(x.day)
d = datetime(1956, 1, 31)
print(d)
t = datetime(21, 2, 3)
print(t)

# print(dir(datetime))
t = time(22, 10)
print(t)
t = datetime.now()
print(t)
print(t.strftime("%A,%B %d,%Y"))
# str1 = '15 August, 1947'
# d = datetime.strptime(str1, " %d  %B, %Y")
# print(d)

t = datetime(2019, 3, 15)
print(t)

y = 2022
m = 1
print(cl.month(y, m))
y = 2022
print(cl.calendar(y, 2, 1, 6))
print(cl.isleap(y), "not a leap year")
print(cl.leapdays(1947, 2022), "are the number of days")
c = cl.monthrange(2019, 7)
print(c, "#0 is considered as monday")

# ctd = cl.date(y, m, d)
# print(ctd)
e = date.today()
print(e)
