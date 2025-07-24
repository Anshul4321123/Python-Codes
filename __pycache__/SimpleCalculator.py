a=input("The first number:")
operation=input("The operation you want to perform(suitable operation include +,-,*,/,//,%,**): ")
b=input("the second number: ")

if(a.isdigit() and b.isdigit()):
    a=int(a)
    b=int(b)
    if(operation=="+"):
        print(a+b)
    elif(operation=="-"):
        print(a-b)
    elif(operation=='*'):
        print(a*b)
    elif(operation=="/"):
        if(b==0):
            print("I know you are trying to go to infinity.")
        else:
            print(a/b)
    elif(operation=="//"):
        if(b==0):
            print("I know you are trying to go to infinity.")
        else:
            print(a//b)
    elif(operation=="%"):
        if(b==0):
            print("I know you are trying to go to infinity.")
        else:
            print(a%b)    
    elif(operation=="**"):
        num=1
        for i in range(b):
            num=num*a
        print(num)
        
         