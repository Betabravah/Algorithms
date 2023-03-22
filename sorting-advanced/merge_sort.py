def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

def merge(left, right):
    new = []
    p1 = p2 = 0

    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            new.append(left[p1])
            p1 += 1
        else:
            new.append(right[p2])
            p2 += 1

    new.extend(left[p1:])
    new.extend(right[p2:])

    return new

# 4, 3, 4, 6, 7, 1


def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
test()
