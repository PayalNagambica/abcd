#give an inter which prints b is even or odd,
# if it is even and  includes range of 10 to 30 
#  even and less than 10 
#b is even and which is greater than 30


a=int(input('enter integer'))
b=a%2
a=a+1
if(b==1):
    print("b is odd")
elif(b==0):
    if(10<=a<30):
        print('a is even and included in range of 10 t0 30')
    elif(a<10):
        print('a is even and less than 10')
    elif(a>=30):
        print('a is even and greater than or equal to 30')
   
else:
    print('stop')
