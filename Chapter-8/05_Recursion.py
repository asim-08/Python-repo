def factorail (n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorail(n-1)
print(factorail(5))


