age = int(input("Enter you'r age: "))
# if statement 1.
if (age%2 == 0):
    print("a is Even")
# End of if statement 1.

# if statement 2.
if (age>18):
    print("You are above the age of concent")
    print("So You can vote")

elif (age<0):
    print("You are entering an Negative invalid age")

else:
    print("You are below the age of concent")
    print("So You can not vote")
# End of if statement 2.
print("End of program")