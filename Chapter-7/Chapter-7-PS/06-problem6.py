# 5! = 1 X 2 X 3 X 4 X 5 factorial
n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product = product * i
print(f"The factorail of {n} is {product}.")