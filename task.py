# -----------------
# Function 1
# -----------------

hex_dig = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def conv_int(int_str):
    # This function convert string to integer
    num = 0
    for digit in int_str:
        num = 10 * num + hex_dig[digit]
    return num


def conv_float(fl_str):
    # This function convert string to float point number
    dec_idx = fl_str.index('.')
    len_dec = len((fl_str[dec_idx + 1:len(fl_str)]))

    whole_number = conv_int(fl_str[0:dec_idx])
    decimal = conv_int(fl_str[dec_idx + 1:len(fl_str)]) / (10 ** len_dec)

    num = whole_number + decimal
    return num


def conv_hex(hex_str):
    # This function convert hexdecimal string to decimal number
    num = 0
    for i in range(len(hex_str)):
        if hex_str[i] not in hex_dig:
            return None

        power = 16 ** (len(hex_str)-i-1)
        if (len(hex_str)-i) == 0:
            power = 1

        num += hex_dig[hex_str[i]] * power
    return num


def conv_num(num_str):
    # This is the main function 1
    # It will take string, and convert to int, float, and hexdecimal
    if num_str.isdigit():
        return conv_int(num_str)
    if num_str.count('.') == 1:
        return conv_float(num_str)
    if num_str.startswith('0x', 0, 2) and len(num_str) > 2:
        return conv_hex(num_str[2:len(num_str)])
    if num_str.startswith('-0x', 0, 3) and len(num_str) > 3:
        return -conv_hex(num_str[3:len(num_str)])
    return None

# -----------------
# Function 2
# -----------------


mon_list = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
            '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}


def check_year(year):
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    return False


def inside_loop(n, a, b, c):
    global num_sec
    num_sec = n
    global day
    day = a
    global month
    month = b
    global year
    year = c
    if check_year(year) is True:
        if num_sec >= 31622400:
            num_sec = num_sec - 31622400
            year += 1
        else:
            mon_day = mon_list.get(str(month))
            if mon_day == 2:
                mon_sec = (mon_day+1)*86400
            else:
                mon_sec = mon_day*86400

            if num_sec > mon_sec:
                num_sec -= mon_sec
                month += 1
            else:
                if num_sec >= 86400:
                    num_sec -= 86400
                    day += 1
    else:
        if num_sec >= 31536000:
            num_sec = num_sec - 31536000
            year += 1
        else:
            mon_day = mon_list.get(str(month))
            mon_sec = mon_day*86400
            if num_sec > mon_sec:
                num_sec -= mon_sec
                month += 1
            else:
                if num_sec >= 86400:
                    num_sec -= 86400
                    day += 1


def my_datetime(n):
    global num_sec
    num_sec = n
    s = '-'
    global day
    day = 1
    global month
    month = 1
    global year
    year = 1970
    if num_sec == 0:
        result = str(month) + s + str(day) + s + str(year)
    else:
        while(num_sec >= 86400):
            inside_loop(num_sec, day, month, year)
        if month < 10:
            result = '0' + str(month) + s
        else:
            result = str(month) + s
        if day < 10:
            result = result + '0' + str(day) + s
        else:
            result = result + str(day) + s
        result += str(year)
    return result

# -----------------
# Function 3
# -----------------


def conv_endian(num, endian='big'):
    if endian == 'big' or endian == 'little':
        positive = True
        # check negative or positive
        if num < 0:
            positive = False
            num = -num
        result = hexReturn(num)
        # each byte must be two characters in length
        if len(result) % 2 != 0:
            result = '0' + result
        # big or little endian
        result = styleForm(result, endian)
        if positive is True:
            return result
        else:
            return "-" + result
    else:
        return None


def styleForm(result, endian):
    res = ''
    array = []
    tmp = ''
    normal = space(result)
    # break sting into array
    for a in normal:
        if a == ' ':
            array.append(tmp)
            tmp = ''
        else:
            tmp += a
    if tmp:
        array.append(tmp)
    # merge the array
    if endian == 'little':
        for x in array:
            res = str(x) + ' ' + res
    elif endian == 'big':
        res = normal
    return res


def space(result):
    # separated by a space
    res = ''
    for x in range(len(result)):
        if (x % 2 != 0) or (x == 0):
            res = res + result[x]
        elif x % 2 == 0:
            res = res + ' ' + result[x]
    return res


# give the hexadecimal number in big endian
def hexReturn(num):
    result = ""
    if int(num) == 0:
        result = 0
    while num != 0:
        remainder = int(int(num) % 16)
        num = (int(num)-remainder) / 16
        if remainder >= 10:
            # transform the number to character
            remainder = chr(remainder + 55)
        result = str(remainder) + result
    return result
