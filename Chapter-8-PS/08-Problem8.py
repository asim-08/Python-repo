a = int(input("Enter a number: "))
def table(n):
    if n == 0:
        return 0
    for i in range(1,11):
        print(f"{a} X {i} = {a * i}")
table(a)

