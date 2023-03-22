


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
        return (self.lst[self.__len__() - 1])
    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        else:
            return self.lst.pop()

        


def validator(string):
    VStack = StackList()
    Dict = {"(" : ")", "{" : "}", "[" : "]"}
    for i in string:
        if i in "({[":
            VStack.push(i)
        elif i in "}])" and Dict[VStack.top()] == i and VStack.is_empty() == False:
            VStack.pop()
        elif VStack.is_empty() and i == "}])":
            return "Invalid"
    if VStack.is_empty():
        return "valid"
    else:
        return "Invalid"

   
print(validator("(])"))

