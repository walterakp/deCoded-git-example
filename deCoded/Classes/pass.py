class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"Hello my name is {self.name}. I am now {self.age} years old.")

class Location:
    def __init__(self, city, state):
        self.city = city
        self.state = state

class newPerson(Person, Location):
    pass

p1 = newPerson("John", 36)
p1.city = "Lekki"
p1.state = "Lagos"

print(p1.city)
p1.sayHello()