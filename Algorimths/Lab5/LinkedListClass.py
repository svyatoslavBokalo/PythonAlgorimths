class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    # def get_data(self):
    #     return self.__data
    # def set_data(self, data):
    #     self.__data = data
    # def set_node(self, node):
    #     self.__next = node


class LinkedList:

    # def __init__(self, linkedList):
    #     # I think one of the paradigms of OOP says that parameters should be encapsulated
    #     self.__head = Node()

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
        s = ""
        current = self.__head
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



# ll = LinkedList()
# ll.append(1)
# ll.append("Hi!")
# ll.append(3.14)
# ll.display()
# print(ll.read(2))
# print(ll[1])
#
# print(ll.go_to_end())
#
# ll.insert(2, "insert")
# ll.display()
# # ll.insert(5, "insert")
#
# ll.insert_node(43, "insert_node")
# ll.display()
# ll.insert_node(3, 63800)
# ll.display()
# ll1 = LinkedList()
# ll1.insert_node(0, "3.453")
# ll1.display()
#
#
# lst = [3, "rere", "32345", 432.453]
# ll.insert_values(lst)
# ll.display()
#
# ll1 = LinkedList()
# ll1.insert_values(lst)
# ll1.display()
#
# ll.insert_at_head("First")
# ll.display()
#
# ll2 = LinkedList()
# ll2.insert_values([0, 45, "efe"])
# ll2.display()
#
# print()
# print("merge list:")
# ll.merge_lists(ll2)
# ll.display()
#
#
# print()
# print("MODIFY: ")
# ll.modify(0, "I'm Svyat")
# ll.display()
#
# print()
# ll.modify(3, "I'm Svyat")
# ll.display()
#
# print()
# ll.modify(ll.length() - 1, "the last")
# ll.display()
#
# print()
# print("DELETE: ")
# ll.delete(2)
# ll.display()
#
# print()
# ll.delete(0)
# ll.display()
#
# print()
# ll.delete(ll.length()-1)
# ll.display()
#
# print()
# print("REVERSE: ")
# ll.reverse()
# ll.display()
# lst = [3, "rere", "32345", 432.453]
# ll1 = LinkedList()
# ll1.insert_values(lst)
# ll1.display()
# ll2 = LinkedList(ll1)
# ll2.display()

# print("----")
# # print([node.data for node in ll1])
# for i in ll1:
#     print(i)

# lst = [3, "rere", "32345", 432.453]
# ll = LinkedList()
# for el in lst:
#     ll.append(el)
# ll.display()
# print()
# ll1 = LinkedList(ll)
# ll1.display()



