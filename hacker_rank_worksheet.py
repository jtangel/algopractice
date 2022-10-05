
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



# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from 0 to 100.
# Any grade less than  40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (grades[i] + 2) % 5 == 0 or (grades[i] + 1) % 5 == 0:
                grades[i] = (round(grades[i]/5.0) * 5)
    return grades


print(gradingStudents([73, 67, 38, 33]))


# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

#  info on hackerank website

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesForSam = 0
    orangesForSam = 0
    for i in apples:
        if (a + i) in range(s, t+1):
            applesForSam += 1
    for x in oranges:
        if (b+x) in range(s, t+1):
            orangesForSam += 1
    print(applesForSam)
    print(orangesForSam)
        

# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

def kangaroo(x1, v1, x2, v2):
    jumps = []
    isPossible = False
    for i in range(0,10001):
        x1 += v1
        jumps.append(x1)
        x2 += v2
        jumps.append(x2)
    print(jumps)
    for x in range(len(jumps) - 1):
        if jumps[x] == jumps[x +1]:
            isPossible = True
    if isPossible == True:
        return 'YES'
    else: return 'NO'



