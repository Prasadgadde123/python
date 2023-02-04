str=input("enter a string")
abc = str.split()
print(*abc)
vowels="aeiou"
for i in abc:
    count=0
    ex = i
    for char in ex:
        if char in vowels:
            count=count+1    
            ex = ex.replace(char,"")

    if count==len(i):
        print(i,end="")
    else:
        print(ex,end=" ")

    