def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(0)
        return
    elif n == 2:
        print("Fibonacci sequence up to", n, ":")
        print(0, 1)
        return

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    print("Fibonacci sequence up to", n, ":")
    print(*fib_sequence)    


x=input("")
fibonacci(int(x))