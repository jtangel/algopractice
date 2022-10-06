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
        