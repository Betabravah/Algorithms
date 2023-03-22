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
        self.size += 1
    def size(self):
        return self.size

    def GetValues(self):
        values = []
        current = self.head
        while current != None:
            values.append(current.value)
            current = current.next
        return values

    def removeEverySecond(self):
        current = self.head
        second = current.next

        while second != None and second.next != None:
            current.next = second.next
            current = second.next
            second = current.next

            


def main():
    lst = linked_list()
    lst.addlast(0)
    lst.addlast(1)
    lst.addlast(2)
    lst.addlast(3)
    print(lst.GetValues())
    lst.addmiddle('a', 2)
    print(lst.GetValues())
    print(lst.size)
    lst.removeEverySecond()
    print(lst.GetValues())


main()
