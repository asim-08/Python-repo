import os

# Specify the path of the directory
path = "/Users"  # current directory; you can also use something like "C:/Users/YourName/Documents"

# Get list of files and directories
contents = os.listdir(path)

# Print the contents
print("Contents of directory:", path)
for item in contents:
    print(item)
