number=int(input('enter a number'))
if number <= 1:
    print('invalid number')
if number == 2:
    print('prime')
else:
      for i in range(2,number):
        if number % i==0:
            print('not prime')
            break
        else:
            print('prime')  
            break  


