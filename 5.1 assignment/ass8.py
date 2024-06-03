def outer():
    def inner():
        return "Hello core2web"
    
    return inner
    print("In outer")

if __name__=='__main__':
    result=outer()()
    print(result)
    