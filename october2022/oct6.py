# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered

# The integer being considered is a factor of all elements of the second array

# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

def getTotalX(a, b):
    total = 0
    for i in range (1,101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            total += 1
    return total

print(getTotalX([2,4], [16,32,96])) 
print(getTotalX([100,99,98,97,96,95,94,93,92,91], [1,2,3,4,5,6,7,8,9,10]))


