a=input("enter a string")
b=len(a)

for x in range(b):
    if x< b-1:
        if a[x]== a[x+1]:
            print(a[x],"is duplicated")
    else:
        if a[-1]==a[0]:
            print(a[x],"is duplicated")
