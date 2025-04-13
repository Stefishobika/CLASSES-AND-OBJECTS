a=input("enter a string")
count=0
print("The consonants are:")
for x in a:
    if x in ["a","e","i","o","u","A","E","I","O","U"]:
        count+=1
    elif x in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]:
        print(x)
    else:
        print("INVALID INPUT")
print("The no of vowels are:",count)

        
