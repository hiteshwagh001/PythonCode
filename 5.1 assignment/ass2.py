def add(x):
    def inner(y):
        print("value of x : ",x)
        return x*y 
    print("in add")
    return inner

if __name__=='__main__':
    add3=add(3)
    result =add3(7)
    print(result)
    print(__file__)
    print(__package__)
    