# 3 = 1 * 2 *3
# 5 = 5 * 4 * 3 * 2 * 1

def fact(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result
print(fact(5))