import hashlib
class Transaction:
    def __init__(self, str = ""):
        # if(str != ""):
        #     arr = str.split(";")
        #     self.__number = int(arr[0])
        #     self.__timeStr = arr[1]
        #     self.__dateStr = arr[2]
        #     self.__from = arr[3]
        #     self.__to = arr[4]
        #     self.__amount = float(arr[5])
        #     self.__hasd_value =
        # else:
        #     raise ValueError("inccorect data")
        if (str == ""):
            raise ValueError("inccorect data")
        arr = str.split(";")
        self.__number = int(arr[0])
        self.__timeStr = arr[1]
        self.__dateStr = arr[2]
        self.__from = arr[3]
        self.__to = arr[4]
        self.__amount = float(arr[5])

        hashStr = str(self.__number) + str(self.__timeStr) + str(self.__dateStr) + str(self.__from) + str(self.__to) + str(self.__amount)
        encoded = hashStr.encode()
        self.__hash_value = hashlib.sha256(encoded).hexdigest()

    # def __get_Hash_Value(self):
    #     hashStr = str(self.__number) + str(self.__timeStr) + str(self.__dateStr) + str(self.__from)+str(self.__to)+str(self.__amount)
    #     encoded = hashStr.encode()
    #     return hashlib.sha256(encoded).hexdigest()

    def get_hash(self):
        return self.__hasd_value
    def __str__(self):
        return str(self.__number) + " " + self.__timeStr + \
               " " + self.__dateStr + " "+ self.__from + "->" + self.__to + " " + str(self.__amount)

