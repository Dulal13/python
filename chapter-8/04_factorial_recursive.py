def factorial_recursive(n):
    if(n == 0):
        return 1
    else:
        return n*factorial_recursive(n-1)

a = factorial_recursive(5)
print(a)
