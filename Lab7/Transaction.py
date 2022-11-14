class Transaction:
    def __init__(self, str = ""):
        if(str != ""):
            arr = str.split(";")
            self.__number = int(arr[0])
            self.__timeStr = arr[1]
            self.__dateStr = arr[2]
            self.__from = arr[3]
            self.__to = arr[4]
            self.__amount = float(arr[5])
        else:
            raise ValueError("inccorect data")

    def __str__(self):
        return str(self.__number) + " " + self.__timeStr + \
               " " + self.__dateStr + " "+ self.__from + "->" + self.__to + " " + str(self.__amount)

