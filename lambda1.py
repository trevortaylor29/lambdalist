def testfunc(num):
    return lambda x: x*num

result10 = testfunc(10)

print(result10(9))

numbers = [2,6,8,10,11,4,12,7,13,17,0,3]

filtered = list(filter(lambda num: (num>7), numbers))

print(filtered)

mapped = list(map(lambda num: num % 2, numbers))

print(mapped)