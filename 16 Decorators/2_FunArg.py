def normalFun(*args):
    sumData=0
    for i in args:
        sumData+=i
        
    return sumData


print(normalFun(10,20,30,40,50))



def normalFunArgs(**args):
    sumData=0
    for k,v in args.items():
        sumData += v
        
    return sumData

print(normalFunArgs(x=10,y=100,z=200))