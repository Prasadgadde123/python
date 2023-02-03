val=int(input("Enter val: "))
temp=val
sum=0
while(val>0):
    rem=val%10
    sum=sum*10+rem
    val=val//10
if(temp==sum):
    print("Given number is palindrome")  
else:
    print("Given number is not palindrome")      
