# after the last yield do not write any print line to avoid errors
def fun(x,y):
    print("start fun")
    while(x<y):
        yield x
        x+=1
    print("end fun")

for val in fun(1,11):
    print(val)

print("\n\n")

# handled case
def run(x,y):
    print("start run")
    while(x<y):
        yield x
        x+=1
    print("end run")
    yield
    
ret=run(1,5)
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
next(ret)

