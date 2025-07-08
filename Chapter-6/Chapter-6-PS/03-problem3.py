message = input("Enter you message: ")
m1 = "make a lot of money"
m2 = "buy now"
m3 = "subscribe this"
m4 = "click this"
if m1 in message or m2 in message or m3 in message or m4 in message:
    print("This is spam")
else:
    print("This is not spam")