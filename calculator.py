from decimal import Decimal

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a % b != 0:
        c = divmod(a, b)
        return str(c[0])+"."+str(c[1])
    else:
        return a / b