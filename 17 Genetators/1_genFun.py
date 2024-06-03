def genFun(x,y):
    print("in genFun")
    yield x
    yield y
    
ret=genFun(10,20)

for data in ret:
    print(data)
