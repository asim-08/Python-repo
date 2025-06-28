age = int(input("Enter you'r age: "))
# "if" "elif" "else" ladder.
if (age>18):
    print("You are above the age of concent")
    print("So You can vote")

elif (age<0):
    print("You are entering an Negative invalid age")

elif(age==0):
    print("You are entering 0 which is invalid age")

else:
    print("You are below the age of concent")
    print("So You can not vote")

print("End of program")