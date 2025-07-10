class employee:
    # name = "Asim"
    language = "Python"    # These are all class attribute.
    salary = 1200000
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

asim = employee()
asim.language = "Javascript"   # This is a instance attribute.
# print( asim.language, asim.salary)
asim.greet()
asim.getinfo()
# employee.getinfo(asim)