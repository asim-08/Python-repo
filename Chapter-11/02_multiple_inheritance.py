class Employee:
    company = "Arzan.tech"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company name is {self.company}")
class Coder:
     language = "Python"
     def printLanguages(self):
          print(f"Out of all the languages here is the language : {self.language}")

class Programmer(Employee, Coder):
    company = "Arzan.Infotech"
    def showLanguage (self):
            print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()