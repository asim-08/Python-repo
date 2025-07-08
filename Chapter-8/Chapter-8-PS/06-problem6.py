n = float(input("Enter value in inches: "))
def inch_to_cm(n):
    if n == 0:
        return 0
    else:
        return n * 2.54
print(inch_to_cm(n))