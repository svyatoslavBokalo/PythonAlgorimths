from Lab7.Transaction import *
from Algorimths.Algorimths.Lab5.LinkedListClass import *
import hashlib
class Block:
    def __init__(self, block_number, previous_hash, trans1, trans2, trans3, hash):
        self.__block_number = block_number
        self.__previous_hash = previous_hash
        self.__transaction1 = trans1
        self.__transaction2 = trans2
        self.__transaction3 = trans3
        self.__hash = hash
        if(block is not None):
            block = Block(0, 0, 0 ,0 ,0, block)
            self.__block_number = block.get_block_number()
            self.__previous_hash = block.get_previous_hash()
            self.__transaction1 = block.get_transaction1()
            self.__transaction2 = block.get_transaction2()
            self.__transaction3 = block.get_transaction3()
            self.__hash = block.get_hash()
            return
        else:
            if (block_number < 0):
                raise IndexError("inccorect block number")
            self.__block_number = block_number
            if (self.__block_number != 0):
                self.__previous_hash = previous_hash
            else:
                self.__previous_hash = ""
            self.__transaction1 = trans1
            self.__transaction2 = trans2
            self.__transaction3 = trans3
            hashStr = repr(self.__block_number) + repr(self.__transaction1.get_hash()) + \
                      repr(self.__transaction2) + repr(self.__transaction3.get_hash())
            encoded = hashStr.encode()
            self.__hash = hashlib.sha256(encoded).hexdigest()


    def get_block_number(self):
        return self.__block_number

    def get_previous_hash(self):
        return self.__previous_hash

    def get_transaction1(self):
        return self.__transaction1

    def get_transaction2(self):
        return self.__transaction2

    def get_transaction3(self):
        return self.__transaction3

    def get_hash(self):
        return self.__hash

    def get_hash_str(self):
        return str(self.__hash)

    def __str__(self):
        return f'*****Block{str(self.__block_number)}***** \n' \
               f'PrevHash: {str(self.__previous_hash)} \n' \
               f'Tr1: {str(self.__transaction1)}\n' \
               f'Tr2: {str(self.__transaction2)}\n' \
               f'Tr3: {str(self.__transaction3)}\n' \
               f'Hash: {str(self.__hash)}'


