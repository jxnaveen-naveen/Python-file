a=int(input())
b=int(input())
operation=input("SUM/SUB/mul/div:")
if(operation=="SUM"):
    print(a+b)
elif(operation=="SUB"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid operation")
