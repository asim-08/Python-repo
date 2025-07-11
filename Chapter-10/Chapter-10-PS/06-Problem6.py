from random import randint

class train:
    def __init__(slf, trainno):
        slf.trainno = trainno
    def book(self, fro, to):
        print(f"Ticket is book in train no: {self.trainno} from {fro} to {to}")
    def getstatus(self, fro, to):
        print(f"train no: {self.trainno} from {fro} to {to} is running on time")
    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(200, 550)}")

t = train(1454)
t.book("karachi", "Lahore")
t.getstatus("karachi", "Lahore")
t.getfare("karachi", "Lahore")