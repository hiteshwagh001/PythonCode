# * * * 
# * * *
# * * *
for i in range(3):
    # print(i)
    for j in range(3):
        print("*",end=" ")
    print()
print()



# 1 2 3
# 4 5 6
# 7 8 9
num=1
for i in range( 3):
    for j in range(3):
        print(num,end=" ")
        num+=1
    print()
print()


# 0 0 0
# 1 1 1
# 2 2 2
for i in range(3):
    for j in range(3):
        print(i,end=" ")
    print()
print()


# 1 2 3
# 1 2 3
# 1 2 3
for i in range( 3):
    num=1
    for j in range(3):
        print(num,end=" ")
        num+=1
    print()
print()



# A
# B C
# D E F
num=65
for i in range(3):
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print()
print()


# 1 2 3
# 4 5
# 6
num=1
for i in range(3):
    for j in range(3-i):
        print(num,end=" ")
        num+=1
    print()
print()
print()