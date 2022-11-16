from Lab5.LinkedListClass import *
from Lab7_2.Transaction import *
from Lab7_2.Block import *
import hashlib
class Shell_blockchain:
    def __init__(self):
        self.__linkedList = LinkedList()

    def ReadFromFile(self, fileName = "Transactions.csv"):
        lst = LinkedList()
        file = open(fileName, "r")
        lines = file.readlines()
        transaction1 = Transaction(lines[0])
        transaction2 = Transaction(lines[1])
        transaction3 = Transaction(lines[2])
        hashStr = repr(0) + repr(transaction1.get_hash()) + \
                  repr(transaction2.get_hash()) + repr(transaction3.get_hash())
        encoded = hashStr.encode()
        hash = hashlib.sha256(encoded).hexdigest()
        block = Block(0, "", transaction1, transaction2, transaction3, hash)

        self.__linkedList.append(block)

        k = 1
        for i in range(3, len(lines), 3):
            prev_hash = hash
            transaction1 = Transaction(lines[i])
            transaction2 = Transaction(lines[i+1])
            transaction3 = Transaction(lines[i+2])
            hashStr = repr(0) + repr(transaction1.get_hash()) + \
                      repr(transaction2.get_hash()) + repr(transaction3.get_hash())
            encoded = hashStr.encode()
            hash = hashlib.sha256(encoded).hexdigest()
            block = Block(k, prev_hash, transaction1, transaction2,
                          transaction3, hash)
            self.__linkedList.append(block)
            k += 1
        file.close()

    def __str__(self):
        return self.__linkedList.display1()


shell = Shell_blockchain()
shell.ReadFromFile()
print(shell.__str__())