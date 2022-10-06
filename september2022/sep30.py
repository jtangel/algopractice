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

