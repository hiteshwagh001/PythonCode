x=int(input("enter start num"))
y=int(input("enter start num"))

for i in range(x,y+1):
    if(i%3==0 and i%5==0):
        print(i,end=" ")