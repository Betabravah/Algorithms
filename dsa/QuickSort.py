def QuickSort(listToSort):
    if(len(listToSort) <= 1 ):
        return listToSort
    pivot = listToSort.pop()
    leftHalf = []
    rightHalf = []
    for i in range(len(listToSort)):
        if(listToSort[i] < pivot):
            leftHalf.append(listToSort[i])
        else:
            rightHalf.append(listToSort[i])
        
    return QuickSort(leftHalf) + [pivot] + QuickSort(rightHalf)

print(QuickSort([4,1,3,2])) 