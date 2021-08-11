a = int(input('Enter number1 : '))
b = int(input('Enter number2 : '))
c = int(input('Enter number3 : '))
d = int(input('Enter number1 : '))

if(a > b and a > c and a>d):
    print("Max number is : " ,a)
elif (b > c and b >d):
     print("Max number is : " ,b)
elif(c>d):
     print("Max number is : " ,c)
else:
     print("Max number is : " ,d)