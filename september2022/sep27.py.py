
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













