# class QueueList:
#     def __init__(self):
#         self.lst = []
#     def enqueue(self, value):
#         self.lst.append(value)
#     def dequeue(self):
#         return self.lst.pop(0)
#     def is_empty(self):
#         return len(self) == 0
        

class queue:
    def __init__(self, size):
        self.lst = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.rear == self.front == -1:
            self.front =self.rear = 0
            self.lst[0] = value
        elif self.rear == len(self.lst) - 1:
            return "queue overflow"
        else:
            self.rear += 1
            self.lst[self.rear] = value

    def dequeue(self):
        if self.rear == self.front:
            return "empty queue"
        else:
            self.front += 1

    def size(self):
        return self.rear - self.front + 1

    def is_empty(self):
        if (self.rear == -1 == self.front == -1) or (self.front > self.rear):
            return True


myqueue = queue(10)
myqueue.enqueue(1)
myqueue.enqueue(1)
myqueue.enqueue(1)
myqueue.enqueue(1)
myqueue.enqueue(1)
print(myqueue.enqueue(1))
print(myqueue.lst)

myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
print(myqueue.lst)



class circularQueue:
    def __init__(self, size):
        self.lst = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.front == self.rear == -1:
            self.front = self.rear = 0
            self.lst[0] = value
        elif self.front == self.rear + 2:
            return "full queue"
        elif (self.rear == len(self.lst) - 1) and self.front == 0:
            return "full queue"
        else:
            if self.rear < len(self.lst) - 1:
                self.rear += 1
                self.lst[self.rear] = value
            else:
                if (self.rear % (len(self.lst) - 1)) < self.front - 1:
                    self.rear = (self.rear) % (len(self.lst) - 1)
                    self.lst[self.rear] = value

    def dequeue(self):
        if self.front == self.rear == -1:
            return "empty queue"
        elif self.front < (len(self.lst) - 1):
            self.front += 1
        else:
            self.front = (self.front) % (len(self.lst) - 1)



CQueue = circularQueue(10)
CQueue.enqueue(1)
CQueue.enqueue(2)
CQueue.enqueue(3)
CQueue.enqueue(4)
CQueue.enqueue(5)
CQueue.enqueue(6)
CQueue.enqueue(7)
CQueue.enqueue(8)
CQueue.enqueue(9)
CQueue.enqueue(10)


print(CQueue.front)
CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
print(CQueue.front)

CQueue.enqueue(11)
CQueue.enqueue(12)
CQueue.enqueue(13)
CQueue.enqueue(14)
print(CQueue.rear)


CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
CQueue.dequeue()
print(CQueue.front)



print(CQueue.lst)
