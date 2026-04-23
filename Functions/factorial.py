
def fact(n):
    count = n-1
    factorial = n
    for i in range(n):
        if count > 0:
            factorial = factorial * count
            count -= 1
    return factorial
print(fact(10))