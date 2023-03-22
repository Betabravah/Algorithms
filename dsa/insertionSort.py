def insertion(lst):
    for currentIndex in range(1, len(lst)):
        current = lst[currentIndex]
        previousIndex = currentIndex - 1
        while previousIndex >= 0 and lst[previousIndex] > current:
            lst[previousIndex + 1] = lst[previousIndex]
            previousIndex -= 1
        lst[previousIndex + 1] = current
    return lst


lst = [8,2,4,1,3]
print(insertion(lst))