with open("log.txt") as f:
    content = f.read()
if ("Python" in content):
    print("Yes Python is present in content")
else:
    print("No python is not present in content")