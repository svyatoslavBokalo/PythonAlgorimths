import math

# my merge)
def MergeCountInversioun(A, p, q, r):
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
    # input start point for merge k = p
    k = p
    inv = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv += len(L) - i

        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k +=1


    while j < len(R):
        A[k] = R[j]
        j += 1
        k +=1
    return inv



def MergeSortCountInversion(A, p, r):
    res = 0
    if p < r:
        q = (p + r)//2
        inv1 = MergeSortCountInversion(A, p, q)
        inv2 = MergeSortCountInversion(A, q+1, r)
        res = inv1 + inv2 + MergeCountInversioun(A, p , q ,r)

    return res


def BuildDifference(masA, masB):
    masM = [0]*len(masA)

    for i in range(0, len(masA)):
        masM[masA[i] - 1] = masB[i]
    print("masM = ",masM)
    return masM


def CalculateCollaborativeFiltering(inv, n):
    res = (1-2*inv/(n*(n-1)))*100
    return round(res)

#for read from file
def ReadFromFile(str = "C:\\Users\\PC\\source\\PythonWork\\Algorimths\\input_1000_100.txt"):
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

print("start program ------")
print()
print("input number from 1 to 1000")
a = int(input())
print("input again number from 1 to 1000")
b = int(input())
mas1 = TakeOneMas(a)
mas2 = TakeOneMas(b)
masM = BuildDifference(mas1, mas2)
res = MergeSortCountInversion(masM, 0, len(masM) - 1)
print("inv = ", res)
sum = CalculateCollaborativeFiltering(res, len(masM))
print("sum = ", sum, "%")
print()
print("end program ------")

print()
print("TEST -----")
masA = [3, 2, 4, 5, 1]
masB = [2, 5, 3, 1, 4]
masC = [5, 3, 4, 1, 2]
print("masA = ", masA)
print("masB = ", masB)
print("masC = ", masC)
masM = BuildDifference(masA, masB)
masM1 = BuildDifference(masA, masC)

print("count inversion check:")
res = MergeSortCountInversion(masM, 0, len(masM) - 1)
print("M = ", masM)
print("inv = ", res)
sum = CalculateCollaborativeFiltering(res, len(masM))
print("sum = ", sum, "%")

print()
print("count inversion check:")
res = MergeSortCountInversion(masM1, 0, len(masM1) - 1)
print("M1 = ", masM1)
print("inv = ", res)
sum = CalculateCollaborativeFiltering(res, len(masM1))
print("sum = ", sum, "%")
print()
print("TEST END!")