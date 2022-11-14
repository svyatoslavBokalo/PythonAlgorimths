import math
#from pythonds.basic.stack import Stack

# this method for priority operations
def priorityOperations(operations):
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
def CreatePoland(formula):
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
                  priorityOperations(stack[-1]) > priorityOperations(el)):
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