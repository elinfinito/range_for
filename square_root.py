    minValue = 4
    maxValue = 18
    sumValue = range(minValue, maxValue)
    sumValue = sumValue [0::2]
    import math
    for i in sumValue:
        print(math.sqrt(i))

    #или
    print("")
    #или

    minValue = 4
    maxValue = 18
    sumValue = range(minValue, maxValue)
    sumValue = sumValue[0::2]
    for i in sumValue:
        print(i ** 0.5)
