class employee:
    # name = "Asim"
    language = "Python"    # These are all class attribute.
    salary = 1200000
asim = employee()
asim.language = "Javascript"   # This is a instance attribute.
print( asim.language, asim.salary)
