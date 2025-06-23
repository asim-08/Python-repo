a = (1, 2, 5, 605.45, False, "Asim", "sudais")
print(a)
no = a.count(5)
print(no)
print(a.index("Asim"))
print(len(a))
print(605.45 in a)
print(a * 2)



b = (1, 2, 3,)
a, _, c = b      # This is the method of unpacking tuple.
print(a, c)