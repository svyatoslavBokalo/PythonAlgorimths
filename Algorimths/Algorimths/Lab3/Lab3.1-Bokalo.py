import math

# my merge)
def Merge(A, p, q, r):
    nl = q-p+1
    nr = r-q

    L = []
    R = []
    for i in range(0, nl):
        L.append(A[p+i])
    for i in range(0, nr):
        R.append(A[q+1 + i])

    i = 0
    j = 0
    # input start point for merge
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k +=1


    while j < len(R):
        A[k] = R[j]
        j += 1
        k +=1

def MergeSort(A, p, r):
    if p < r:
        q = (p + r)//2
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p , q ,r)

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


mas = [5, 3, 1 ,2 ,4]
print(mas)
MergeSort(mas, 0, len(mas) - 1)
print(mas)

print("input number from 1 to 1000")
a = int(input())
#take one mas with number a in file
mas1 = TakeOneMas(a)
print(mas1)
MergeSort(mas1, 0, len(mas1) - 1)
print(mas1)