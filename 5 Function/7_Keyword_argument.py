def fun(**argv):
    print(type(argv))
    print(argv)

fun(x=10,y=30)
# fun(10,20,30)         throws error typeerror


print("\n\n=============================\n\n")

def fun2(x,y,**argv):
    print(x)
    print(y)
    for key,value in argv.items():
        print(key," : ",value)

        
fun2(x=10,y=20,z=30)