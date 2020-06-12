class MyClass:
    x = 5
    z = "Hello"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"Hello my name is {self.name}. I am now {self.age} years old.")
        
p1 = Person("John", 36)
print (p1.age)

p1.age+=10
p1.sayHello()

