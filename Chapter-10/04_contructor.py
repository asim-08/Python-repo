class employee:
    # name = "Asim"
    language = "Python"    # These are all class attribute.
    salary = 1200000

    def __init__(self, name, salary, language):   # Dundr method which is automatically called.
            print("I am creting an object")
            self.name = name
            self.salary = salary
            self.language = language

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

asim = employee("Harry", 1300000, "javascript")
asim.name = "Asim"
print( asim.name, asim.salary, asim.language)
# asim.language = "Javascript"   # This is a instance attribute.
# asim.greet()
# asim.getinfo()
# employee.getinfo(asim)