# i=5
def fun():
    j=1
    for i in range(1,11):
        nonlocal j
        print(j+1)
        print(i)
    print(j)
fun()