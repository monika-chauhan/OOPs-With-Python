class Animal:
    def speak(self):
        print("animal Speaking ")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barking")

d = Dog()
d.speak()

        