#append string input from user in next lines of file


while True:
    a=input("enter something")
    print(a)
    f=open('p.txt',"a")
    f.write(a+'\n')
    f.close()
    f=open('p.txt','r')
    print(f.read())
    f.close()