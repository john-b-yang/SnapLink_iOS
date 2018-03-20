import math

def square_root(x):
    print('Square Root Called')
    y = math.sqrt(x)
    return y

def squared(x):
    print('Squared Called')
    y = x * x
    return y

def factorial(x):
    if (x == 1):
        return x
    else:
        return x * factorial(x - 1)
