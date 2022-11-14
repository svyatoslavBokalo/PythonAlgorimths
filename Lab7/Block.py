from Lab7.Transaction import *
from Lab5.LinkedListClass import *
class Block:
    def __init__(self, block_number, previous_hash, trans1, trans2, trans3, hash):
        self.__block_number = block_number
        self.__previous_hash = previous_hash
        self.__transaction1 = trans1
        self.__transaction2 = trans2
        self.__transaction3 = trans3
        self.__hash = hash

    

    def __str__(self):
        return f'*****Block{str(self.__block_number)}***** \n ' \
               f'PrevHash: {str(self.__previous_hash)} \n' \
               f'Tr1: {str(self.__transaction1)}\n' \
               f'Tr2: {str(self.__transaction2)}\n' \
               f'Tr3: {str(self.__transaction3)}\n' \
               f'Hash: {str(self.__hash)}'

