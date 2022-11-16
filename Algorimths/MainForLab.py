# main for lab 2
def mainForLab2():
    try:
        formula = "(20+31)*(3*12-4/3)"
        print("formula = ", formula)
        res = CreatePoland(formula)
        print(res)
        calculateRes = Calculate(formula)
        print("res = ", calculateRes)
        print()

        formula1 = "12+2*((3*4)+(10:5))"
        print("formula = ", formula1)
        res = CreatePoland(formula1)
        print(res)
        calculateRes = Calculate(formula1)
        print("res = ", calculateRes)
        print()

        formula2 = "12 + 2 * ( ( 3 * 4 ) + ( 10 / 5 ) )"
        print("formula = ", formula2)
        res = CreatePoland(formula2)
        print(res)
        calculateRes = Calculate(formula2)
        print("res = ", calculateRes)
        print()

        formula3 = "1/0"
        print("formula = ", formula3)
        res = CreatePoland(formula3)
        print(res)
        calculateRes = Calculate(formula3)
        print("res = ", calculateRes)
        print()
    except ZeroDivisionError as x:
        print(x)

def mainForLab3():
    mas = [5, 3, 1 ,2 ,4]
    print(mas)
    # MergeSort(mas, 0, len(mas) - 1)
    MergeSort(mas, 0, len(mas) - 1)
    print(mas)

    print("input number from 1 to 1000")
    a = int(input())
    mas1 = TakeOneMas(a)
    print(mas1)
    MergeSort(mas1, 0, len(mas1) - 1)
    print(mas1)


def CreatePoland(formula):
    polishFormula = ""
    operations = ["+", "-", "*", "/", ":", "^"]
    stack = []

    count = len(formula)

    # to run throto read a char in a formula
    while (count > 0):
        el = formula[len(formula) - count]

        # check if element is a number
        if (str(el).isnumeric()):
            polishFormula += el
        else:
            polishFormula += " "

        # check if element is '('
        if (el == '('):
            stack.append(el)

        # check if elemetn is ')'
        if (el == ')'):
            k = len(stack)
            while stack[k - 1] != '(':
                element = stack.pop()
                polishFormula += element + " "
                k -= 1
            stack.pop()

        # if element is operation then
        if (operations.__contains__(el)):
            while (len(stack) != 0 and
                   priorityOperations(stack[-1]) > priorityOperations(el)):
                element = stack.pop()
                polishFormula += element + " "

            stack.append(el)

        count -= 1

    # and the last operations write down in queue and polishFormula: string
    while (len(stack) != 0):
        element = stack.pop()
        polishFormula += element + " "

    # remove empty space
    lst = polishFormula.split()
    res = ""
    for el in lst:
        res += el + " "
    res = res[:-1]

    return res