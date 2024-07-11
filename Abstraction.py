from abc import ABC,abstractmethod
class Car(ABC):
    # abstract method 
    def milage(self):
        pass 

class Tesla(Car):
    def milage(self):
        print("Tesla Car milage is : 3.3Km/hr")

class Tata(Car):
    def milage(self):
        print("Tata car milage is: 4Km/hr")

tesla = Tesla()
tata = Tata()
tesla.milage()
tata.milage()