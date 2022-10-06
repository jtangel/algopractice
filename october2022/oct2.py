# # Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# # Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# # - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock



def timeConversion(s):
    newString = ''
    if s[-2] == 'A' and s[0] == '1':
        newString = '00' + s[2:8]
        return newString
    elif s[-2] == 'A':
        newString = s[:8]
    elif s[-2] == 'P' and s[:2] == '12':
        newString = s[:8]
    else:
        x = int(s[:2]) + 12
        y = s[2:8]
        newString = (f'{x}{y}')
    return(newString)



print(timeConversion('12:01:00AM'))
print(timeConversion('01:00:00AM'))
print(timeConversion('06:40:03AM'))
print(timeConversion('11:00:00PM'))
print(timeConversion('12:45:54PM'))