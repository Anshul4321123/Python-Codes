def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a = input("Enter Number:")
if a.isdigit():
    a=int(a)
    b=factorial(a)
    print(f"The factorail of {a} is {b}")
else:
    print("Please enter a valid number")
