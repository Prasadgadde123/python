str=input("enter string:")
count=0
for i in range(0,int(len(str)/2)):
    if(str[i]!=str[len(str)-i-1]):
        count=1
if(count==0):
    print('Palindrome')
else:
    print("non palindrome")    