def fun(*argv):
    print(type(argv))
    for i in argv:
        print(i)
        
fun(10,20,30,40)
print("=============================\n\n")
def fun2(x,y,*argv):
    print(x)
    print(y)
    print(argv)
    for i in argv:
        print(i)
fun2(10,20,30,40,50)

print("=============================\n\n")
def fun3(*argv,x,y):
    print(x )
    print(y)
    for i in argv:
        print(i)

# fun3(10,20,30,40,50)  throws error

