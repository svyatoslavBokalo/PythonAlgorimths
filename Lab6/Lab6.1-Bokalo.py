
# luna algorimth
def AlgorimthOfLuna(number: str):
    # check if card is existed
    if(checkCardIsExist(number) == False):
        return

    sum = 0
    number = str(number)
    lenghtOfNumber = len(number)
    # print("lenghtOfNumber = ", lenghtOfNumber)
    i = 1


    while(lenghtOfNumber > 0):
        el = number[lenghtOfNumber-1]
        # print("el = ", el)
        if(i % 2 == 0):
            n = int(el)*2
            # print("n = ", n)
            if(int(n) >= 10):
                sum += int(n) - 9
                # print("sum = ", sum)
            else:
                sum+= int(n)
                # print("sum = ", sum)
        else:
            sum += int(el)
            # print("sum = ", sum)

        lenghtOfNumber -= 1
        i += 1

    if(sum % 10 == 0):
        # print("True")
        return checkWhatIsCard(number)

    # print("false")
    return "INVALID"

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

def checkCardIsExist(number: str):
    n = len(number)
    if(n == 13 or n == 15 or n == 16):
        if(number.isdigit() == False):
            return False
        else:
            return True

    return False


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