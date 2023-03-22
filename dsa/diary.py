"""
SECTION - 2

1. Bethelhem Yemane - UGR/1894/13 
2. Habiba Nesro     - UGR/0088/13 
3. Leul Wujira      - UGR/8834/13 
4. Rihana Ersanu    - UGR/8031/13 
5. Sarah Ayele      - UGR/0948/13 
6. Thomas Wondwosen - UGR/1972/13
"""

import copy
from datetime import datetime

class StackEmpty(Exception):
    def __init__(self, msg="Stack is empty"):
        Exception.__init__(self, msg)


class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        if self.isEmpty():
            raise StackEmpty
        return self.data.pop()
    
    def peek(self):
        if self.isEmpty():
            raise StackEmpty
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0
    
    def length(self):
        return len(self.data)

class EditHistory:
    def __init__(self):
        self.diaryStates = Stack()
    
    def storeState(self, diarystate, description):
        state = (copy.deepcopy(diarystate), description)
        self.diaryStates.push(state)
    
    def undo(self):
        if not self.diaryStates.isEmpty():
            return self.diaryStates.pop()        

class Diary:
    def __init__(self):
        self.pages = PageList()
    
    def add(self, title, content, date=datetime.now()):
        self.pages.addPageLast(title, content, date)

    def removeByPageNo(self, pageNo):
        self.pages.removeByPageNo(pageNo)

    def getTitles(self):
        return self.pages.getTitles()

    def sortTitles(self):
        return self.pages.sort()
    
    def searchByPage(self, pageNumber):
        return self.pages.searchByPageNo(pageNumber)

    def searchByTitle(self, title):
        return self.pages.searchByTitle(title)
    
    def searchByDate(self, date):
        return self.pages.searchByDate(date)

    def getTotalPages(self):
        return self.pages.size
    

class Page:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content        
        self.date = date
        self.prev = None
        self.next = None
        

class PageList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def addPageLast(self, title, content, date): # since a diary page is written day after day, we can only add at last
        newPage = Page(title, content, date)
        if self.size == 0:
            self.head = self.tail = newPage            
            self.size += 1
        else:
            newPage.prev = self.tail            
            self.tail.next = newPage
            self.tail = newPage
            self.size += 1

    def removeByPageNo(self, pageNo):
        node_to_remove = self.searchByPageNo(pageNo)
        if node_to_remove:
            self.removeNode(node_to_remove)

    def removeNode(self, page): 
        if page not in self:
            return 

        if page == self.head and page == self.tail:
            self.tail = self.head = None
            self.size -= 1           
            return

        if page == self.head:
            self.head = self.head.next
            self.head.prev = None
        
        elif page == self.tail:            
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:                    
            page.prev.next = page.next
            page.next.prev = page.prev
        
        self.size -= 1
        
    def getTitles(self):
        if self.size == 0:
            return None
        else:
            current = self.head
            titles = []
            while current:
                titles.append(current.title)
                current = current.next
            return titles

    def searchByTitle(self, title):
        match = PageList()
        current = self.head
        while current:
            if title.lower() in current.title.lower():
                match.addPageLast(current.title, current.content, current.date)
            current = current.next
        return match        

    def searchByPageNo(self, pageNo):
        if pageNo > self.size:
            return

        i = 1
        current = self.head
        while current != None:
            if i == pageNo:
                return current
            current = current.next
            i += 1  

    def getPageNumber(self, page):
        pageNo = 1
        current = self.head
        while current != page and pageNo <= self.size:            
            current = current.next
            pageNo += 1
        
        if pageNo <= self.size:
            return pageNo

    def searchByDate(self, date):
        current = self.head
        while current != None:            
            if current.date.date() == date.date():
                return current
            current = current.next

    def sort(self):
        current = self.head
        titles = []
        while current != None:
            titles.append(current.title)
            current = current.next
        return self.mergeSort(titles)

    def merge (self, list1, list2):
        merged_list = []
        while (len(list1) != 0 and len(list2) != 0):
            i = 0
            if list1[i] <= list2[i]:
                merged_list.append(list1[i])
                del list1[i] 
            else:
                merged_list.append(list2[i])
                del list2[i]
        if len(list1) == 0:
            merged_list += list2
        elif len(list2) == 0:
            merged_list += list1
        return (merged_list)

    def mergeSort (self, lst):
        if len(lst) == 1:
            return lst
        else:
            left = lst [len(lst) // 2:]
            right = lst[:(len(lst) // 2)]
            return  self.merge(self.mergeSort (right), self.mergeSort(left))
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


if __name__ == "__main__":
    new = Diary()

    new.add("first", "bla bla")
    new.add("second", "baaa")
    new.add("third", "biiii")
    new.add("abc", "beeee")
    print(new.searchByPage(1).title)
    print(new.sortTitles())
    print(new.getTotalPages())
    new.removeByPageNo(2)
    print(new.getTotalPages())
    print(new.sortTitles())
    new.removeByPageNo(4)
    print(new.getTotalPages())
    print(new.sortTitles())

    while new.pages.head:
        print(new.pages.head.title)
        new.removeByPageNo(1)
    print([n.title for n in new.pages], new.getTotalPages())
        
    
