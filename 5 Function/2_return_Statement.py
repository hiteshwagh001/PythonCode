def fact(num):
    if(num==1):
        return 1
    return num*fact(num-1)

num=int(input("enter number to calculate factorial : "))
print("factorial of ",num,"is",fact(num))