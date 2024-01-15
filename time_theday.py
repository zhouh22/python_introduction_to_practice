import time

now = time.strftime("%Y/%m/%d")
year, month, day = now.split("/")
year = int(year)
month = int(month)
day = int(day)


def is_leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    else:
        return False


def count_day(y, m, d):
    today = d
    if is_leap_year(y):
        lis = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    else:
        lis = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    for i in range(m):
        today += lis[i]
    print("{}".format(today))


count_day(year, month, day)
