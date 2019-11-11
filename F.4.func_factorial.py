def factorial(x):
    if(x==0):
        return x+1
    elif(x==1):
        return x
    else:
        return x * factorial(x-1)
print(factorial(3))
