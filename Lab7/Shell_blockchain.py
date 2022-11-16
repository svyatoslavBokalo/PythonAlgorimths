from Algorimths.Algorimths.Lab5.LinkedListClass import *
from Lab7.Transaction import *
import hashlib
class Shell_blockchain:
    def __init__(self):
        self.__linkedList = LinkedList()

    def ReadFromFile(self, fileName = "Transactions.csv"):
        file = open(fileName, "r")
        lines = file.readlines()
        transaction1 = Transaction(lines[0])
        transaction2 = Transaction(lines[1])
        transaction3 = Transaction(lines[2])

        block = Block(0, "", transaction1, transaction2, transaction3, )
        print(transaction)
        file.close()

shell = Shell_blockchain()
shell.ReadFromFile()