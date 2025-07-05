print("Even or Odd Checker")
x=input("please enter a number: ")
if x.isdigit():
    x=int(x)
    if(x%2==0):
        print("Even")
    else:
        print("Strange the number is not divisible by 2")