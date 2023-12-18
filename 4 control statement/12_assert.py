name=input('Enter your Name: ')
age=int(input("enter your age : "))

assert age>0 ," age can't be -ve"
if(age>18):
    print(name,"is  eligible for voting")
else:
    print(name,"is not eligible for voting")
