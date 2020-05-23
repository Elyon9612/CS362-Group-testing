import unittest
import random

mon_list = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
            '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}


def check_year(year):
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                return True
    return False


def my_datetime(num_sec):
    s = '-'
    day = 1
    month = 1
    year = 1970
    if num_sec == 0:
        result = str(month) + s + str(day) + s + str(year)
    else:
        while(num_sec >= 86400):
            if check_year(year) is True:
                if num_sec > 31622400:
                    num_sec -= 31622400
                    year += 1
                mon_day = mon_list.get(str(month))
                if mon_day == 2:
                    mon_sec = (mon_day+1)*86400
                else:
                    mon_sec = mon_day*86400
                if num_sec > mon_sec:
                    num_sec -= mon_sec
                    month += 1
                if num_sec >= 86400:
                    num_sec -= 86400
                    day += 1
            else:
                if num_sec > 31536000:
                    num_sec -= 31536000
                    year += 1
                mon_day = mon_list.get(str(month))
                mon_sec = mon_day*86400
                if num_sec > mon_sec:
                    num_sec -= mon_sec
                    month += 1
                if num_sec >= 86400:
                    num_sec -= 86400
                    day += 1
        if month < 10:
            result = '0' + str(month) + s
        else:
            result = str(month) + s
        if day < 10:
            result = result + '0' + str(day) + s
        else:
            result = result + str(day) + s
        result += str(year)
    print result
    return result


if __name__ == '__main__':
    main()
