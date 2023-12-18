list=["aakash","sudama","kadam",'bagul'];
name=input("enter your name : ")
flag=0;
for i in list:
    if(name==i):
        flag=1;
        print(name,"is present in list")
else:
    print(name ," is not present in list")


if( name not in list):
    print(name ," is not present in list")
else:
    print(name ," is present in list")

