from Lab7_2.Transaction import *
def ReadFromFile(fileName ="Transactions.csv"):
    mas = []
    file = open(fileName, "r")
    lines = file.readlines()
    # print(lines)

    for line in lines:
        transaction = Transaction(line)
        mas.append(transaction)

    file.close()

    return mas

print("hellllooooo")
mas = ReadFromFile()
for i in mas:
    print(i)