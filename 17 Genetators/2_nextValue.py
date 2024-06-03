def genFun(x,y):
    print("in genFun")
    yield x
    yield y
    
ret=genFun(10,20)
print(type(genFun))     # show <class'function'>
print(next(ret))
print(next(ret))
print(type(ret))        # show <class'generator'>