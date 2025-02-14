from random import randint

class Train:
    
    def __init__(self, train_number):
        self.train_number = train_number

    def book(self,from_station, to_station):
        print(f"Ticket booked for train number {self.train_number} from {from_station} to {to_station}")

    def getStatus(self):
        print(f"Train number {self.train_number} is running on time")

    def getFare(self, from_station, to_station):
        print(f"The fare for train number {self.train_number} from {from_station} to {to_station} is ${randint(100, 1000)}")

t = Train(30158)
t.book( "New York", "Washington")
t.getStatus()
t.getFare( "New York", "Washington")