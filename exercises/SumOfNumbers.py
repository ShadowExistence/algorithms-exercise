def SumOfNaturalNumbers():
    x = 0
    for i in range(0, 10000):
        if( i % 7 == 0 or i % 9 == 0):
            x += i
    return x

print(SumOfNaturalNumbers())