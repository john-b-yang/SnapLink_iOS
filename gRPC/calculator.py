import math, base64

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

def rotateImage(x):
    # X is a hash code
    png_recovered = base64.decodestring(x)
    temp_image = open('temp.png', 'wb')
    temp_image.write(png_recovered)
    return x
