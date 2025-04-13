a=input("enter main string:")
b=input("enter tring 1:")
c=input("enter string 2:")
if b in a:
    print("its a substring")
elif(c in a):
    c=a
    print(c)
else:
    print("a is not a substring")
'''for x in range(len(a)):
    for y in range(len(b)):
        if a[x]==b[y]:print("substring of a")
        else:print("its not a substring")
    for z in range(len(c)):
        if a[x]==c[z]:
            c=a
print(c)'''
