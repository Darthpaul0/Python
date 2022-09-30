# Create a class Person with the attribute name
# and the method talk()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'My name is {self.name}')


persona = Person("Jack")
persona2 = Person("John")

persona.talk()
persona2.talk()
