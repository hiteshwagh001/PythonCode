import sys 

print(sys.argv)

size=len(sys.argv)

for val in range(0,size):   
    print(sys.argv[val])
    
# python3 1_cmdArgv.py 10 20 30    run this line