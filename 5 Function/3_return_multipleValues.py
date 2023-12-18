def addByTen(x,y,z):
    x=x+10
    y+=10
    z+=10

    return x,y,z

def returnBytuple(x,y,z):
    x=x+10
    y+=10
    z+=10

    return x,y,z

x=10
y=20
z=30

a,b,c=addByTen(x,y,z)


print(a)
print(b)
print(c,"\n\n")


tupleOutput=addByTen(x,y,z)
for i in tupleOutput:
    print("value ",i)