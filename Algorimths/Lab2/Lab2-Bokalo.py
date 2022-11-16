import math
def gettokens(operations):
    res = 0
    # check what is this operation
    if(operations == "+"):
        res = 0
    elif(operations == "-"):
        res = 0
    elif (operations == "*"):
        res = 1
    elif (operations == "/"):
        res = 1
    elif (operations == ":"):
        res = 1
    elif (operations == "^"):
        res = 1

    return res

# method which change formula into polis notation
def infixtopostfix(formula):
    polishFormula = ""
    operations = ["+", "-", "*", "/", ":", "^"]
    stack = []
    formula += " "
    i = 0
    # to run throto read a char in a formula
    while(i< len(formula)):
        el = formula[i]

        #check if element is a number
        if (str(el).isnumeric()):
            polishFormula += el
        else:
            polishFormula += " "

        #check if element is '('
        if (el == '('):
            stack.append(el)

        # check if elemetn is ')'
        if (el == ')'):
            k = len(stack)
            while stack[k-1] != '(':
                element = stack.pop()
                polishFormula += element + " "
                k -= 1
            stack.pop()

        # if element is operation then
        if (operations.__contains__(el)):
            while(len(stack) != 0 and
                  gettokens(stack[-1]) > gettokens(el)):
                element = stack.pop()
                polishFormula += element + " "

            stack.append(el)

        i += 1


    #and the last operations write down in queue and polishFormula: string
    while(len(stack) != 0):
        element = stack.pop()
        polishFormula += element + " "


    # remove empty space
    lst = polishFormula.split()
    res = ""
    for el in lst:
        res+=el+" "
    res = res[:-1]

    return res

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
def calculator(formula):
    res = 0
    stack = []
    operations = ["+", "-", "*", "/", ":", "^"]
    mas = infixtopostfix(formula).split()

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


# use the try block for check on divide by zero
try:
    formula = "(20+31)*(3*12-4/3)"
    print("formula = ", formula)
    res = infixtopostfix(formula)
    print(res)
    calculateRes = calculator(formula)
    print("res = ", calculateRes)
    print()

    formula1 = "12+2*((3*4)+(10:5))"
    print("formula = ", formula1)
    res = infixtopostfix(formula1)
    print(res)
    calculateRes = calculator(formula1)
    print("res = ", calculateRes)
    print()

    formula2 = "12 + 2 * ( ( 3 * 4 ) + ( 10 / 5 ) )"
    print("formula = ", formula2)
    res = infixtopostfix(formula2)
    print(res)
    calculateRes = calculator(formula2)
    print("res = ", calculateRes)
    print()

    formula3 = "1-2-3"
    print("formula = ", formula3)
    res = infixtopostfix(formula3)
    print(res)
    calculateRes = calculator(formula3)
    print("res = ", calculateRes)
    print()

    formula4 = "1/0"
    print("formula = ", formula4)
    res = infixtopostfix(formula4)
    print(res)
    calculateRes = calculator(formula4)
    print("res = ", calculateRes)
    print()
# if in formula is dividing by zero generate an exception
except ZeroDivisionError as x:
    print(x)