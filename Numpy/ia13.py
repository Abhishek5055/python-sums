def fibonacci_while(n):
    a, b = 0, 1
    i = 2
    while i <= n:
        a, b = b, a + b
        i += 1
    return b

n = int(input("Enter the value of n: "))
result = fibonacci_while(n)
print(f"The {n}th Fibonacci number is {result}")
