def outer():
    count=10
    
    def inner():
        nonlocal count
        count+=1
        print('inner ',count)
        return count
    
    print("outer : ",count)
    return inner

if __name__=='__main__':
    counter=outer()
    print(counter())
    print(counter())
    
counter1=outer()
counter1()
