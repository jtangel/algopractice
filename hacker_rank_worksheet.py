
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if i == j:
                sum1 += arr[i][j]
            if i + j == (len(arr) - 1):
                sum2 += arr[i][j]
    return abs(sum1 - sum2)


print(diagonalDifference(((11,2,4), (4,5,6), (10,8,-12))))



def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in range (len(arr)):
        if arr[i] > 0:
            pos += 1/len(arr)
        if arr[i] < 0:
            neg += 1/len(arr)
        if arr[i] == 0:
            zer += 1/len(arr)
    print(format(pos,'.6f'))
    print(format(neg,'.6f'))
    print(format(zer,'.6f'))


plusMinus((-4, 3, -9, 0, 4, 1))


# # Its base and height are both equal to n It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# # Write a program that prints a staircase of n size .

def staircase(n):
    stairs = ''
    for i in range(1, n + 1):
        stairs = ('#' * i) 
        print(f'{stairs :>{n}}')
        

staircase(6)

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.



def miniMaxSum(arr):
    maxi = 0
    mini = 0
    x = min(arr)
    y = max(arr) 
    for i in range(len(arr) - 1):
        if arr[i] == x and arr[i] == y:
            maxi += arr[i]
            mini += arr[i]
    for i in range(len(arr)):
        if arr[i] != x:
            maxi += arr[i]
        if arr[i] != y:
            mini += arr[i]
    print(mini, maxi)


miniMaxSum([5,5,5,5,5])
miniMaxSum([1,2,3,4,5])


# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.




def birthdayCakeCandles(candles):
    byeFire = 0
    max_height = max(candles)
    for i in range(len(candles)):
        if candles[i] == max_height:
            byeFire += 1
    print(byeFire)
    return byeFire


birthdayCakeCandles([1,4,4,4,3,2])


# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock



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


