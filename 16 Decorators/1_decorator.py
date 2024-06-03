def decorFun(fun):
    print("Inside decorator function")
    def wrapper():
        print("Start")
        fun()
        print("end")
    return wrapper;


@decorFun
def normalFun():
    print("in normal fun")

# normalFun=decorFun(normalFun)

normalFun()