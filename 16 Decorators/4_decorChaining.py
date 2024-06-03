def decorFun(fun):
    def wrapper():
        print("Start wrapper")
        fun()
        print("end wrapper")
    return wrapper

def decorRun(func):
    def wrapper1():
        print("Start wrapper 1")
        print("-----------------")
        func()
        print("-----------------")
        print("End wrapper 1")
    return wrapper1
        
@decorFun
@decorRun
def normalFun():
    print("In normal Fun")
    
normalFun()
    
# def normalFun():
#     print("In normal Fun")
# normalFun=decorFun(decorRun(normalFun))