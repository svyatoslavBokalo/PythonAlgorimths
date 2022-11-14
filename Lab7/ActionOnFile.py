from Lab7.Transaction import *
def ReadFromFile(str = "Transactions.csv"):
    mas = []
    file = open(str, "r")
    lines = file.readlines()
    # print(lines)

    for line in lines:
        transaction = Transaction(line)
        mas.append(transaction)
    # for line in file:
    #     arr = line[:-1].split(";")
    #

    # for i in range(0, countline):
    #     line = file.readline()
    #     arr = line.split()
    #     row = []
    #     for j in range(1, countFilm + 1):
    #         row.append(int(arr[j]))
    #
    #     mas.append(row)

    file.close()

    return mas

print("hellllooooo")
mas = ReadFromFile()
for i in mas:
    print(i)