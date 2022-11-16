import hashlib
class Transaction:
    def __init__(self, variable =""):
        # if(variable != ""):
        #     arr = variable.split(";")
        #     self.__number = int(arr[0])
        #     self.__timeStr = arr[1]
        #     self.__dateStr = arr[2]
        #     self.__from = arr[3]
        #     self.__to = arr[4]
        #     self.__amount = float(arr[5])
        #     self.__hasd_value =
        # else:
        #     raise ValueError("inccorect data")
        self.__number = 0
        self.__timeStr = ""
        self.__dateStr = ""
        self.__from = ""
        self.__to = ""
        self.__amount = 0
        self.__hash_value = ""
        if (variable == ""):
            raise ValueError("inccorect data")
        elif(isinstance(variable, str)):
            arr = variable.split(";")
            self.__number = int(arr[0])
            self.__timeStr = arr[1]
            self.__dateStr = arr[2]
            self.__from = arr[3]
            self.__to = arr[4]
            self.__amount = float(arr[5])

            hashStr = repr(self.__number) + repr(self.__timeStr) + repr(self.__dateStr) + \
                      repr(self.__from) + repr(self.__to) + repr(self.__amount)
            encoded = hashStr.encode()
            self.__hash_value = hashlib.sha256(encoded).hexdigest()
            return
        # elif(variable is Transaction):
        #     variable = Transaction(variable)
        #     self.__number = variable.get_number()
        #     self.__timeStr = variable.get_timeStr()
        #     self.__dateStr = variable.get_dataStr()
        #     self.__from = variable.get_from()
        #     self.__to = variable.get_to()
        #     self.__amount = variable.get_amount()
        #     self.__hash_value = variable.get_hash()
        #     return

    # def __get_Hash_Value(self):
    #     hashStr = variable(self.__number) + variable(self.__timeStr) + variable(self.__dateStr) + variable(self.__from)+variable(self.__to)+variable(self.__amount)
    #     encoded = hashStr.encode()
    #     return hashlib.sha256(encoded).hexdigest()
    def get_number(self):
        return self.__number

    def get_timeStr(self):
        return self.__timeStr

    def get_dataStr(self):
        return self.__dateStr

    def get_from(self):
        return self.__from

    def get_to(self):
        return self.__to

    def get_amount(self):
        return self.__amount
    def get_hash(self):
        return self.__hash_value

    def get_str_hash(self):
        return str(self.__hash_value)
    def __str__(self):
        return str(self.__number) + " " + self.__timeStr + \
               " " + self.__dateStr + " "+ self.__from + "->" + self.__to + " " + str(self.__amount)



trans = Transaction("1;12:30;06.10.2022;Maria;Xrystya;0.002")
print(trans.__str__())