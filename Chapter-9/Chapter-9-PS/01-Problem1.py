f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("The words twinkle is present in the content")
else:
    print("There word twinkle is not present in the content")

f.close()
