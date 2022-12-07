import math
from Algorimths.lab1JustPolishNotation import *


#this method for operations on numbers
# and pass
# the first number is a
# second number is b
# third its operation
def JustOperationsWithDigit(a, b, operations):
    res = 0
    #check what is this operation
    if(operations == '+'):
        res = a + b
    elif (operations == '-'):
        res = a - b
    elif (operations == '*'):
        res = a * b
    elif (operations == '/' or operations == ':'):
        if b == 0:
            raise ZeroDivisionError("!!! divide by zero !!!")
        else:
            res = a / b
    elif (operations == '^'):
        res = math.pow(a, b)

    return res

# in this method we calculate our formula
def Calculate(formula):
    res = 0
    stack = []
    operations = ["+", "-", "*", "/", ":", "^"]
    mas = CreatePoland(formula).split()

    # read all element of massive ib polish notation
    for i in range(0, len(mas)):
        if(str(mas[i]).isnumeric()):
            stack.append(mas[i])

        # check if element of massive is operation
        if(operations.__contains__(mas[i])):
            b = float(stack.pop())
            a = float(stack.pop())
            res = JustOperationsWithDigit(a, b, mas[i])
            stack.append(res)

    return round(res)

