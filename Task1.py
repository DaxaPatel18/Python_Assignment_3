def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"Factorial of {n} is : {fact}")

n=int(input("Enter a number:"))
factorial(n)

