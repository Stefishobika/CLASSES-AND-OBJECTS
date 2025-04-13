a=input("enter a string")
b=input("enter a string")
for x in range(len(a)):
    for y in range(len(b)):
        if a[x]==b[y]:
            print(a[x],"the common element")
