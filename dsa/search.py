def linear_search (lst, numberToFind):
    for i in range(len(lst)):
        if lst[i] == numberToFind:
            return "number found"
    return "number not found"

lst = [12, 5, 3, 78, 0]
print(linear_search(lst, 78))


def binary_search(lst, numberToFind):
    start = 0
    last = len(lst) - 1
    while start <= last:
        mid = (start + last) // 2
        if lst[mid] == numberToFind:
            return mid
        if lst[mid] < numberToFind:
            start = mid +1
        else:
            last = mid - 1

    return -1

print(binary_search(lst, 0))

            
        
            