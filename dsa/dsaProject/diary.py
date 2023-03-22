class Diary:
    def __init__(self):
        self.pages = pageList()
    
    def add(self, title, content):
        self.pages.addPageLast(title, content)

    def removeByPageNo(self, pageNo):
        self.pages.removeByPageNo(pageNo)

    def removeByTitle(self, title):
        self.pages.removeByTitle(title)

    def getTitles(self):
        return self.pages.getTitles()

    def sortTitles(self):
        return self.pages.sort()

    def searchByTitle(self, title):
        return self.pages.searchByTitle(title)

    def getTotalPages(self):
        return self.pages.size

class page:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.prev = None
        self.next = None
        self.pageNumber = 0

class pageList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def addPageLast(self, title, content): # since a diary page is written day after day, we can only add at last
        newPage = page(title, content)
        if self.size == 0:
            self.head = self.tail = newPage
            newPage.pageNumber += 1
            self.size += 1
        else:
            newPage.prev = self.tail
            newPage.pageNumber = self.tail.pageNumber + 1
            self.tail.next = newPage
            self.tail = newPage
            self.size += 1

    def removeByPageNo(self, pageNo):
        if pageNo < 1 or pageNo > self.tail.pageNumber:
            return "Invalid Page Number!"
        else:
            if self.size == 0:
                return "The diary contains no pages"
            elif self.size == 1:
                self.head = self.tail = None
                self.size -= 1
            elif self.size > 1 and pageNo == 1:
                self.head = self.head.next
            else:
                current = self.searchByPageNo(pageNo)
                current.prev.next = current.next
                current.next.prev = current.prev

    def removeByTitle(self, title):
        if title in self.getTitles():
            current = self.searchByTitle(title)
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            return "Title Not Found!"

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
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return "No page with the give title"

    def searchByPageNo(self, pageNo):
        current = self.head
        while current != None:
            if current.pageNumber == pageNo:
                return current
            current = current.next
        return "No page with the give page number"

    def sort(self):
        current = self.head
        titles = []
        while current != None:
            titles.append(current.title)
            current = current.next
        return (self.mergeSort(titles))

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

new = Diary()

new.add("first", "bla bla")
new.add("second", "baaa")
new.add("third", "biiii")
new.add("abc", "beeee")
print(new.getTotalPages())
new.removeByPageNo(2)
new.removeByTitle("third")
print(new.sortTitles())

