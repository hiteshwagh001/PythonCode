# pass 
# it passes only if else block and excutes further code after if else
for i in range(1,10):
    if(i%2==0):
        pass
    else:
        print(i)
    print("Hello")
print()
print()

# Continue
# it continues the if else block and not excutes any further code in this block

for i in range(1,16):
    if(i%5==0):
        continue
    else:
        print(i)
    print("Hello")
print()
print()


# Break
# it breaks the loop and excutes the further code after the loop

for i in range(1,16):
    if(i%5==0):
        break
    else:
        print(i)
    print("Hello")
print()
print()