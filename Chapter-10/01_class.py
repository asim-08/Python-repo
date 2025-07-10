class employee:
    # name = "Asim"
    language = "Python"    # These are all class attribute.
    salary = 1200000
asim = employee()
asim.name = "Asim"   # This is a object attribute.
print(asim.name, asim.language, asim.salary)
rohan = employee()
rohan.name = "Robinson"   # This is also a instance attribute.
print(rohan.name, rohan.salary, rohan.language)
# Here name is object attribute and salary and language are class attributes as the directly belong to the class.