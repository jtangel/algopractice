# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,

# The sum of the integers on the squares is equal to his birth day.

# Determine how many ways she can divide the chocolate.

# s = list with integers
# d = birthday
# m = birthmonth

# write a for loop that loops through all of s and takes all possibilities of values that sum to d



def birthday(s, d, m):
    total = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            total += 1
    return total

# print(birthday([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1], 18, 7))
# print(birthday([4], 4, 1))
# print(birthday([1,2,1,3,2], 3, 2))


# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i < j  and ar[i] + ar[j] is divisible by k.

def divisibleSumPairs(n, k, ar):
    total = 0
    for i in range (n):
        for j in range (n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                total += 1
    return total



