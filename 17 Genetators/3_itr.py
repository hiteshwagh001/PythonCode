def fun():
    print("start")
    yield 10
    yield 20
    yield 30
    print("end")

for i in fun():
    print(i)

print("\n\n")
def run():
    print("start")
    yield 510
    yield 520
    yield 530
    print("end")

ret =fun()
print(next(ret))
print(next(ret))
print(next(ret))
# print(next(ret))  this line throws error and not giving us proper answer 

    