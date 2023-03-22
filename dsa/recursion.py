def countdown(number):
    if number == 0:
        print (0)
    else:
        print(number)
        countdown(number - 1)
countdown(10)


def string_reverse(string):
    if len(string) == 1:
        return string
    else:
        rreversed = string[-1] + string_reverse(string[1:-1]) + string[0]
        return rreversed
print(string_reverse("betty"))


def sumDigits(num):
    if num < 10:
        return num
    else:
        sum = (num % 10) + sumDigits(num // 10)
        return sum

print(sumDigits(123))


def GCD(num1, num2):
    if num2 == 0:
        return num1
    else:
        return GCD(num2, num1 % num2)

def LCM(num1, num2):
    return (num1 * num2) / (GCD(num1, num2))

print(LCM(12,6))

def isListSorted(lst):
    if len(lst) <= 1:
        return True
    else:
        return lst[0] < lst[1] and isListSorted(lst[1:])
    

lst = [1,2,3]
lst2 = [2,6,4]

print(isListSorted(lst))
print(isListSorted(lst2))

