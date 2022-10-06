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

