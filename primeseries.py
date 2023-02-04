start=int(input('Enter start number'))
end=int(input('Enter end number'))
for i in range(start,end):
    flag=0
    for j in range(2,i):
            if i%j==0:
                flag=1
                break
    if flag==0:
        print(i,end=' ')