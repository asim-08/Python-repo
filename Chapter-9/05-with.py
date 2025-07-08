f = open("file.txt")
print(f.read())
f.close()

# The same task can be done using with statement like this :
with open("file.txt") as f:
    print(f.read())
# You don't have need to close the file.