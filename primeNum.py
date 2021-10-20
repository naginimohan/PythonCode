num = int(input('Enter your number :\n'))
flag = False
if(num > 1):
    for i in range(2,num):
        if( num % i == 0):
            flag = True 
            break

if flag:
    print(num,'number is prime')
else:
    print(num,'number is not prime')