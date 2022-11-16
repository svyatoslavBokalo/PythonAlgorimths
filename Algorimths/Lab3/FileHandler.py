#for read from file
def ReadFromFile(str):
    mas = []
    file = open(str, "r")
    str = file.readline()

    countline = int(str.split()[0])
    countFilm = int(str.split()[1])

    for i in range(0,countline):
        line = file.readline()
        arr = line.split()
        row = []
        for j in range(1, countFilm+1):
            row.append(int(arr[j]))

        mas.append(row)

    file.close()

    return mas

# for print all mas in file
def PrintMatrix(mas):
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            print(mas[i][j], " ", end="")

        print()

# for take one mas with a certain number in file
def TakeOneMas(number):
    mas = ReadFromFile("C:\\Users\\PC\\source\\PythonWork\\Algorimths\\input_1000_100.txt")
    return mas[number-1]