
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


# print(diagonalDifference(((11,2,4), (4,5,6), (10,8,-12))))



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


# plusMinus((-4, 3, -9, 0, 4, 1))


# Its base and height are both equal to n It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of n size .

def staircase(n):
    stairs = ''
    for i in range(1, n + 1):
        stairs = ('#' * i) 
        print(f'{stairs :>{n}}')
        

staircase(6)