from Lab7.Block import *
from Lab7.ActionOnFile import *

class Blockchain:
    def __int__(self):
        self.__block = []

    def __create_block(self):
        lst = []
        mas = ReadFromFile()
        for i in range(0, len(mas)):
            if(i == 0):
                block = Block(i, "", Transaction(mas[3*i+1]),
                              Transaction(mas[3*i+2]),
                              Transaction(mas[3*i+3]))