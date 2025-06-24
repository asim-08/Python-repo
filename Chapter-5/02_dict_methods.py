marks = { 
    "Asim": 100,
    "Saim": 50,
    "Sudais": 30,
    0: "Talha"
}
print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sudais": 29, "zaheer": 10})
print(marks)
print(marks.get("adil")) # It will give you a None word when you entered any key that does not exist in the Dictionary.
print(marks["Asim"])     # It will give you a error when you entered any key that does not exist in the Dictionary.
print(marks.copy())
print(marks.pop("Asim"))
print(marks)
print(marks.clear())
print(marks)