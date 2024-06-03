def decorFun(func):
    print("Decor fun")
    def wrapper(*args):
        print("Start Wrapper")
        val=func(*args)
        print(val)
        print("end wrapper")
        return val
    return wrapper

@decorFun
def normalFun(x,y):
    print("Normal fun start")
    return x+y

print(normalFun(10,20))
