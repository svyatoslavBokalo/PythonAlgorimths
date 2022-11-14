from Lab7.Transaction import *
from Algorimths.Algorimths.Lab5.LinkedListClass import *
import hashlib
class Block:
    def __init__(self, block_number, previous_hash, trans1, trans2, trans3):
        if(block_number<0):
            raise IndexError("inccorect block number")
        self.__block_number = block_number
        if(self.__block_number != 0):
            self.__previous_hash = previous_hash
        else:
            self.__previous_hash = ""
        self.__transaction1 = trans1
        self.__transaction2 = trans2
        self.__transaction3 = trans3
        hashStr = str(self.__block_number)+ str(Transaction(self.__transaction1).get_hash())+ str(Transaction(self.__transaction2).get_hash())+ str(Transaction(self.__transaction3).get_hash())
        encoded = hashStr.encode()
        self.__hash = hashlib.sha256(encoded).hexdigest()



    def __get_Hash(self):
        encode = str(self.__block_number)+ str(self.__transaction1)
    def get_hash(self):
        return self.__hash

    def __str__(self):
        return f'*****Block{str(self.__block_number)}***** \n ' \
               f'PrevHash: {str(self.__previous_hash)} \n' \
               f'Tr1: {str(self.__transaction1)}\n' \
               f'Tr2: {str(self.__transaction2)}\n' \
               f'Tr3: {str(self.__transaction3)}\n' \
               f'Hash: {str(self.__hash)}'


