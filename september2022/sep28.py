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
