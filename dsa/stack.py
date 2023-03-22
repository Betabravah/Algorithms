class Empty(Exception):
    pass
class StackList:
    def __init__(self):
        self.lst = []
    def __len__(self): 
        return len(self.lst)
    def is_empty(self):
        return len(self.lst) == 0
    def push(self, value):
        self.lst.append(value)
    def top(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        return self.__len__ - 1
    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        return self.lst.pop()

        

MyStackList = StackList()
MyStackList.push(1)
MyStackList.push(2)
MyStackList.push(3)
MyStackList.push(4)
MyStackList.push(5)
print(MyStackList.pop())
print(MyStackList.pop())
print(MyStackList.pop())
print(MyStackList.__len__())



class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addfirst(self, value):
        newNode = node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.next = self.head
            self.head = newNode
            size += 1
    def addlast (self, value):
        newNode = node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
    def addmiddle(self, value, index):
        newNode = node(value)
        position = 0
        current = self.head
        while position < index - 1:
            current = current.next
            position += 1
        newNode.next = current.next
        current.next = newNode        

    def GetValues(self):
        values = []
        current = self.head
        while current != None:
            values.append(current.value)
            current = current.next
        return values

    def LastElement(self):
        
        return self.tail





class StackLL:
    def __init__(self):
        LL = linked_list()
        self.LL.size = 0

    def len(self):
        return self.LL.size

    def push(self, value):
        return self.LL.addlast(value)

    def pop(self):
        x = self.LastElement



stack1 = StackList()
stack2 = StackList()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(7)
print(stack1.lst)

def removeEverySecond(stack1, stack2):
    if len(stack1.lst) % 2 == 0:
        while stack1.lst != []:
            stack1.pop()
            
        stack2.push(stack1.top)
        stack1.pop()
