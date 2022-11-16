#it's luna algorithm
def AlgorimthOfLuna(number: str):
    # check if card is exist
    if(checkCardIsExist(number) == False):
        return

    sum = 0
    number = str(number)
    lenghtOfNumber = len(number)
    i = 1

    # sum of the algorithm
    while(lenghtOfNumber > 0):
        el = number[lenghtOfNumber-1]
        if(i % 2 == 0):
            n = int(el)*2
            if(int(n) >= 10):
                sum += int(n) - 9
            else:
                sum+= int(n)
        else:
            sum += int(el)

        lenghtOfNumber -= 1
        i += 1

    #chech if sum // 10
    if(sum % 10 == 0):
        return checkWhatIsCard(number)

    return "INVALID"

# function for chech what is this card
def checkWhatIsCard(number:str):
    lenght = len(number)
    # print("number[0:1] = ", number[0:2])
    if(lenght == 15 and (number[0:2] == "34" or number[0:2] == "37")):
        return "American Express"
    if(lenght == 16 and (number[0:2] == "51" or number[0:2] == "52" or number[0:2] == "53"
    or number[0:2] == "54" or number[0:2] == "55")):
        return "MasterCard"
    if((lenght == 16 or lenght == 13) and number[0] == "4"):
        return "Visa"

    return None

# function for chech if card is exist
def checkCardIsExist(number: str):
    n = len(number)
    if(n == 13 or n == 15 or n == 16):
        if(number.isdigit() == False):
            return False
        else:
            return True

    return False


# def fillingNumber(number:variable):
#     sum = 0
#     lenghtOfNumber = len(number)
#     # print("lenghtOfNumber = ", lenghtOfNumber)
#     i = 1
#     indexOfUnknown = -1
#     while (lenghtOfNumber > 0):
#         el = number[lenghtOfNumber-1]
#         if(el.isdigit() == False):
#             indexOfUnknown = i
#         else:
#             if(i % 2 == 0):
#                 n = int(el) * 2
#                 # print("n = ", n)
#                 if (int(n) >= 10):
#                     sum += int(n) - 9
#                     # print("sum = ", sum)
#                 else:
#                     sum += int(n)
#                     # print("sum = ", sum)
#             else:
#                 sum += int(el)
#                 # print("sum = ", sum)
#
#         i += 1
#         lenghtOfNumber -= 1
#
#     remainderSum = 10 - (sum % 10)
#     myDigit = -1
#     if(indexOfUnknown % 2 == 0):
#         # el = number[indexOfUnknown-1]
#         if(remainderSum % 2 == 0):
#             myDigit = remainderSum/2
#             sum += myDigit
#         else:
#             myDigit = (remainderSum+9)/2
#             sum += myDigit
#     else:
#         myDigit = remainderSum
#         sum+= myDigit
#
#
#     return myDigit, sum

def fillingNumber1(number: str):
    sum = 0
    n = len(number)
    res = -1
    index = -1
    for i in range(0, n):
        el = number[i]
        if(el.isdigit() == False):
            index = i

    number2 = ""
    for i in range(n-1, -1, -2):
        el = number[i]
        number2 = el+number2
        if(i - 1) >= 0:
            if (i-1) != index:
                k = int(number[i-1]) * 2
                s = k
                if(k >= 10):
                    s = k-9
                number2 = str(s) + number2
            else:
                number2 = number[index] + number2


    print("number =      ", number)
    print("number2 =     ", number2)
    print("len = ", len(number2))


    for i in range(0, n):
        if(i != index):
            sum+= int(number2[i])

    if((n - index - 1) % 2 == 0):
        index = (sum*9) % 10
    else:
        index = 10 - (sum % 10)
        if(index % 2 == 0):
            print("index = ", index)
        else:
            index = int((index+9)/2)


    print("index = ", index)


number = "378282246310005"
print(AlgorimthOfLuna(number))
number = "371449635398431"
print(AlgorimthOfLuna(number))
number = "378734493671000"
print(AlgorimthOfLuna(number))
number = "5555555555554444"
print(AlgorimthOfLuna(number))
number = "5105105105105100"
print(AlgorimthOfLuna(number))
number = "4111111111111111"
print(AlgorimthOfLuna(number))
number = "4012888888881881"
print(AlgorimthOfLuna(number))
number = "4222222222222"
print(AlgorimthOfLuna(number))
number = "5555555555554445"
print(AlgorimthOfLuna(number))
number = "5555-5555-5555-4444"
print(AlgorimthOfLuna(number))
