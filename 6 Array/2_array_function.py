import array as arr

data =arr.array('i',[10,20,30,40,50,10])
data.append(60)
print(data)

print(data.buffer_info())   # address of 1st ele, no. of elements

print(id(data[0]))
print(id(data)) # address of array

print(data.count(10))

data.extend([70,80,90,100])
print(data)

list=[10,20,30]
data2=arr.array('i',[11,12,14,13])
data2.fromlist(list)
print(data2)


print(data.index(40))

data.insert(7,9000)
print(data)

data.pop()
print(data)

data.append(100)
print(data)

data.remove(100)
print(data)

data.reverse()
print(data)

listdata=data.tolist()
print(listdata)