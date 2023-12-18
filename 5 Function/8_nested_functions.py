def outer():
    def inner():
        print("In inner fun")
    print("In Outer fun")
    inner()
    
outer()    



print("=============================\n\n")


print("Function")
def outer():
    def inner1():
        print("inner1")
    def inner2():
        print("inner2")
        inner1();
    inner2()
    
outer()
# outer().inner1()  attribute Error


print("=============================\n\n")

print("Function")
def outer():
    def inner():
        print("inner")
    print(id(inner))
    print("outer")
    return inner;
  
# outer()  #error
ret=outer()
print(id(ret))
ret()



print("=============================\n\n")

print("Function")
def outer():
    def inner():
        print("inner")
    print(id(inner))
    print("outer")
    return inner();
  
# outer()  #error
outer()

print("\n\n=============================\n")

def outer():
    def inner1(a,b):
        print("inner1")
        return a+b
    def inner2(a,b):
        print("inner2")
        return a-b
    print("outer")
    return inner1,inner2;
    
outer()
retObj=outer()
for inner in retObj:
    print(inner(20,10))
    
print("\nseperate output")
ret1,ret2=outer()
inn1=ret1(10,20)
inn2=ret2(30,20)
print(inn1)
print(inn2)
print(inn1+inn2)