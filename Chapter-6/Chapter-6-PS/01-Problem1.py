a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))
if (a>b and a>c and a>d):
    print("The greatest number is", a)

elif (a == b == c == d):
    print("You are entering the same number")

elif (b>a and b>c and b>d):
    print("The greatest number is", b)

elif (c>a and c>b and c>d):
    print("The greatest number is", c)

else:
    print("The greatest number is", d)