# problem 1
start=100
end=110

for i in range(start, end):
    print(i,end=" ")
print()
print()


# problem 2
start=10
end=20
for i in range(start, end):
    if(i%2==0):
        print(i,end=" ")
print()
print()

# problem 3
start=1
end=10
sum=0;
for i in range(start,end):
    sum+=i
print(sum)
print()


# problem 4
# start=int(input("start "))
# end=int(input("end "))
start=65
end=91
if(start>=65):
    for  i in range(start,end):
        print(i," = ",chr(i))
else:
    print("wrong input")
print()
print()


# program 5
start=1
end=100
for i in range(start,end):
    if(i%7==0 and i%3!=0):
        print(i,end=" ")
print()
print()

# program 6
start="A"
end="Z"
for i in range(ord(start),ord(end)):
    print(chr(i)," = ",i)
print()
print()


# program 7
start=-7
end=8
for i in range(start,end):
    if i>0:
        print(i,end=" ")
print()
print()


# program 8
start=15
end=50
for i in range(start,end):
    if(i%3==0 and i%5==0):
        print(i,end=" ")
print()
print()


# program 9
start=-15
end=50
if(start<0):
    print(-start)
print()
print()


# program 10
start= 1
end=11
product=1
for i in range(start,end):
    if i%2!=0:
        product*=i
print(product)