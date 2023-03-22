def merge (list1, list2):
    merged_list = []
    while (len(list1) != 0 and len(list2) != 0):
        i =0
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


def sort (lst):
    if len(lst) == 1:
        return lst

    else:
        left = lst [len(lst)//2:]
        right = lst[:(len(lst)//2)]
        return  merge(sort (right), sort(left))



list1 = [2,3,7]
list2 = [0,1,4,6]
merge (list1, list2)


print(sort([12,45,2,7,0,122]))