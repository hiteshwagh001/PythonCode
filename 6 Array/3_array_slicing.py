import array as arr

data =arr.array('i',[10,20,30,40,50,10])

for i in data[1::]:
    print(i)
print()
for i in data[1:3:]:
    print(i)
print()
    
for i in data[1:5:1]:
    print(i)
print()
    
