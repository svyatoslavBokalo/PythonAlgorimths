import hashlib

# it's cod from lab 5
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self, linkedList = None):
        # I think one of the paradigms of OOP says that parameters should be encapsulated
        if isinstance(linkedList, LinkedList):
            self.__head = Node()

            ptr = self.__head
            current = linkedList.__head
            # self.__head = current
            while current is not None:
                # print(current.data)
                ptr.next = Node(current.data)
                ptr = ptr.next
                current = current.next

            self.__head = self.__head.next


        else:
            self.__head = None




    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_data = Node(data)
        if (self.__head == None):
            self.__head = new_data
            return
        current = self.__head
        while current.next is not None:
            current = current.next
        current.next = new_data

    # Prints out the linked list in traditional Python list format.
    def display(self):
        lst = []
        current = self.__head
        while current is not None:
            lst.append(current.data)
            current = current.next
        print(lst)

    def display1(self):
        current = self.__head
        s = str(current.data) + "\n\n"
        while current.next is not None:
            current = current.next
            s+= str(current.data) + "\n\n"
        return s

    # Returns the length of the linked list.
    def length(self):
        counter = 0
        current = self.__head
        while current is not None:
            current = current.next
            counter += 1
        return counter

    # Returns the value of the node at 'index'.
    def read(self, index):
        if(self.__head == None):
            print("ERROR: 'Read' Index out of range!")
            return None
        if index >= self.length() or index < 0:
            print("ERROR: 'Read' Index out of range!")
            return None

        counter = 0
        current = self.__head
        while True:
            if counter == index:
                return current.data
            current = current.next
            counter += 1

    def read1(self, index):
        if index >= self.length() or index < 0:
            raise IndexError("'Read' Index out of range!")
        counter = 0
        current = self.__head
        while True:
            current = current.next
            if counter == index:
                return current.data
            counter += 1

    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self, index):
        return self.read(index)

    # Goes to the tail node of the linked list.
    def go_to_end(self):
        return self.read(self.length() - 1)

    # Inserts the node at index 'index'. Reports an error, if the index is out of range.
    def insert(self, index, data):
        if (self.__head == None and index == 0):
            temp = Node(data)
            self.__head = temp
            return
        elif (self.__head == None):
            print("Index out of range!")
            raise IndexError("Index out of range!")

        if index >= self.length() or index < 0:
            print("Index out of range!")
            raise IndexError("Index out of range!")

        temp = Node(data)
        if(index == 0):
            temp.next = self.__head
            self.__head = temp
            return

        current = self.__head
        for i in range(0,index):
            current = current.next

        temp.next = current.next
        current.next = temp

    # Inserts the node at index 'index'. Appends at the end, if the index is out of range.
    def insert_node(self, index, data):
        if index >= self.length() or index < 0:
            self.append(data)
        else:
            self.insert(index, data)

    # def insert_node(self, index, data):
    #     temp = Node(data)
    #
    #     if(self.head == None): # if list was been empty
    #         self.head = temp
    #         return
    #
    #     current = self.head
    #     while current.next is not None:
    #         current = current.next
    #
    #     current.next = temp


    # Appends the nodes at the head of linked list.
    def insert_at_head(self, data):
        return self.insert(0, data)


    # Appends the set of nodes from a list of values.
    def insert_values(self, values):
        if self.__head == None:
            self.__head = Node(values[0])
            current = self.__head
            for i in range(1, len(values)):
                temp = Node(values[i])
                current.next = temp
                current = current.next
            return

        current = self.__head
        while current.next != None:
            current = current.next
        for value in values:
            temp = Node(value)
            current.next = temp
            current = current.next


    def merge_lists(self, lnkdlist):
        current = self.__head
        while current.next != None:
            current = current.next


        lnkdlist = LinkedList(lnkdlist)
        for el in lnkdlist:
            current.next = Node(el)
            current = current.next

        # elementLinkLst = lnkdlist.__head
        # while elementLinkLst.next != None:
        #     elementLinkLst = elementLinkLst.next
        #     current = elementLinkLst

    # Replaces the value of node at index 'index' with the new value 'data'.
    def modify(self, index, data):
        if(index >= self.length() or index < 0):
            return

        ptr = self.__head
        for i in range(0, index):
            ptr = ptr.next

        ptr.data = data




    # Deletes the node at index 'index'.
    def delete(self, index):
        if (index >= self.length() or index < 0):
            return

        if(self.__head == None):
            return

        if(self.length() == 1 and index == 0):
            self.__head == None
            return

        if(index == 0):
            self.__head = self.__head.next
            return


        ptr = self.__head
        for i in range(0, index - 1):
            ptr = ptr.next
        temp = ptr.next
        ptr.next = temp.next


    def __iter__(self):
        ptr = self.__head
        # print(ptr.data)
        while ptr:
            yield ptr.data
            ptr = ptr.next


    def reverse(self):
        res = None
        ptr = self.__head
        while ptr != None:
            temp = ptr
            self.__head = ptr.next
            ptr = self.__head
            temp.next = res
            res = temp

        self.__head = res

# in this class I create Transaction
class Transaction:
    # so I pass the values from file such as....
    def __init__(self, variable =""):
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
            # in this step I search hash in my transaction
            hashStr = repr(self.__number) + repr(self.__timeStr) + repr(self.__dateStr) + \
                      repr(self.__from) + repr(self.__to) + repr(self.__amount)
            encoded = hashStr.encode()
            self.__hash_value = hashlib.sha256(encoded).hexdigest()
            return

    # in this func i return number of transaction
    def get_number(self):
        return self.__number

    # in this func i return time of transaction
    def get_timeStr(self):
        return self.__timeStr

    # in this func i return date of transaction
    def get_dataStr(self):
        return self.__dateStr

    # in this func i return sender of transaction
    def get_from(self):
        return self.__from

    # in this func i return reciever of transaction
    def get_to(self):
        return self.__to

    # in this func i return amount of transaction
    def get_amount(self):
        return self.__amount

    # in this func i return hash of transaction
    def get_hash(self):
        return self.__hash_value

    # in this func i return hash of transaction like string
    def get_str_hash(self):
        return str(self.__hash_value)

    # in this func is converted the transaction in string
    def __str__(self):
        return str(self.__number) + " " + self.__timeStr + \
               " " + self.__dateStr + " "+ self.__from + "->" + self.__to + " " + str(self.__amount)

# in this class I create Block of Blockchain
class Block:
    # intialization class
    def __init__(self, block_number, previous_hash, trans1, trans2, trans3, hash):
        self.__block_number = block_number
        self.__previous_hash = previous_hash
        self.__transaction1 = trans1
        self.__transaction2 = trans2
        self.__transaction3 = trans3
        self.__hash = hash

    # in this func i return block number of block
    def get_block_number(self):
        return self.__block_number

    # in this func i return previous hash of block
    def get_previous_hash(self):
        return self.__previous_hash

    # in this func i return transaction1 of block
    def get_transaction1(self):
        return self.__transaction1

    # in this func i return transaction2 of block
    def get_transaction2(self):
        return self.__transaction2

    # in this func i return transaction3 of block
    def get_transaction3(self):
        return self.__transaction3

    # in this func i return hash of block
    def get_hash(self):
        return self.__hash

    # in this func i return hash of block and convert to string
    def get_hash_str(self):
        return str(self.__hash)

    # in this func is converted the block in string
    def __str__(self):
        return f'*****Block{str(self.__block_number)}***** \n' \
               f'PrevHash: {str(self.__previous_hash)} \n' \
               f'Tr1: {str(self.__transaction1)}\n' \
               f'Tr2: {str(self.__transaction2)}\n' \
               f'Tr3: {str(self.__transaction3)}\n' \
               f'Hash: {str(self.__hash)}'

# it's my blockchain
class Shell_blockchain:
    # i intialization the empty LinkedList()
    def __init__(self):
        self.__linkedList = LinkedList()

    #in this func fills my blockchain from file
    def ReadFromFile(self, fileName = "Transactions.csv"):
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
        # it's "for" for filling my blockchain
        for i in range(3, len(lines), 3):
            # check if in file not left data
            if(len(lines) // 3 == k and len(lines) % 3 == 0):
                # print("just return !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return
            # check if in file left just one string
            elif(len(lines) // 3 == k and len(lines)%3 == 1):
                prev_hash = hash
                transaction1 = Transaction(lines[i])
                transaction2 = ""
                transaction3 = ""
                hashStr = repr(0) + repr(transaction1.get_hash()) + \
                          "" + ""
                encoded = hashStr.encode()
                hash = hashlib.sha256(encoded).hexdigest()
                block = Block(k, prev_hash, transaction1, transaction2,
                              transaction3, hash)
                # print("block = ", block)
                self.__linkedList.append(block)
                return
            # check if in file left just two string
            elif(len(lines) // 3 == k and len(lines)%3 == 2):
                prev_hash = hash
                transaction1 = Transaction(lines[i])
                transaction2 = Transaction(lines[i+1])
                transaction3 = ""
                hashStr = repr(0) + repr(transaction1.get_hash()) + \
                          repr(transaction2.get_hash()) + ""
                encoded = hashStr.encode()
                hash = hashlib.sha256(encoded).hexdigest()
                block = Block(k, prev_hash, transaction1, transaction2,
                              transaction3, hash)
                # print("block = ", block)
                self.__linkedList.append(block)
                return
            else:
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

    # in this func converts the blockchain in string
    def __str__(self):
        return self.__linkedList.display1()


shell = Shell_blockchain()
shell.ReadFromFile()
print(shell.__str__())