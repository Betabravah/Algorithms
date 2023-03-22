def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
        return gcd(num1, num2)


print(gcd(120, 1024))

