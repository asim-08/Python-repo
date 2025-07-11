class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The square is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"The square is {self.n ** 1/2}")
    @staticmethod
    def hello():
        print("Hello!")
c = Calculator(4)
c.hello()
c.square()
c.cube()
c.squareroot()