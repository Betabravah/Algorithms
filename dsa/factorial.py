def factorial(num):
    if num < 0:
        print ("No factorial for negative numbers")
    else:
        if num == 0:
            return 1
        else:
            return num * (factorial(num - 1))
        
    
print(factorial (5))
