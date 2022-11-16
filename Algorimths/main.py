from Lab3 import MergeSort
from Lab3.FileHandler import *
from Lab3.MergeSort import *
from Lab3.FileHandler import *
from Lab4.BinarySearchFile import *
def main():
    mas1 = TakeOneMas(237)
    print(mas1)
    MergeSort(mas1, 0, len(mas1) - 1)
    print(mas1)

    element = 44
    middlePoint = (len(mas1) - 1 + 0)//2
    index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
    print("index = ", index)

    mas1 = [3, 6, 8, 12, 14, 15, 16, 19, 22, 23, 24, 29, 33]
    print(mas1)
    element = 12
    middlePoint = (len(mas1) - 1 + 0) // 2
    index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
    print("index = ", index)
    element = 23
    middlePoint = (len(mas1) - 1 + 0) // 2
    index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
    print("index = ", index)
    element = 7
    middlePoint = (len(mas1) - 1 + 0) // 2
    index = BinarySearch(mas1, element, 0, len(mas1) - 1, middlePoint)
    print("index = ", index)





if __name__ == "__main__":
    main()
