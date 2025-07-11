class programmer:
    def __init__(self, name, salary, company, pin):
        self.name = name
        self.salary = salary
        self.company = company
        self.pin = pin
p1 = programmer("Asim", 1200000, "Google", 7875)
print(p1.name, p1.salary, p1.pin, p1.company)        
p2 = programmer("waqas", 1200000, "Google", 7875)
print(p2.name, p2.company, p2.salary, p2.pin)        