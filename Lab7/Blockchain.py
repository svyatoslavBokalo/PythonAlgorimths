from Lab7.Block import *
from Lab7.ActionOnFile import *


def __create_block():
    lst = []
    mas = ReadFromFile()
    print("len(mas) =", len(mas))
    print("len(mas)//3 = ", len(mas) // 3)
    for i in range(0, len(mas) // 3 + 1):
        if (i == 0):
            block = Block(i, "", Transaction(mas[3 * i + 1]), Transaction(mas[3 * i + 2]), Transaction(mas[3 * i + 3]))
            lst.append(block)
        elif (3 * i + 1 >= len(mas)):
            return lst
        elif (3 * i + 2 >= len(mas)):
            block = Block(i, lst[i-1].get_hash(), Transaction(mas[3 * i + 1]), "", "")
            lst.append(block)
            return lst
        elif (3 * i + 3 >= len(mas)):
            block = Block(i, lst[i-1].get_hash(), Transaction(mas[3 * i + 1]), Transaction(mas[3 * i + 2]), "")
            lst.append(block)
            return lst
        else:
            block = Block(i, lst[i-1].get_hash(), Transaction(mas[3 * i + 1]), Transaction(mas[3 * i + 2]), Transaction(mas[3 * i + 3]))
            lst.append(block)

    return lst

print(__create_block())
# class Blockchain:
#     def __int__(self):
#         self.__block =



