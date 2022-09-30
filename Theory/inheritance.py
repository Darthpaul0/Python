class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Use the pass statement to write empty classes
    def bark(self):
        print("Guau!")


class Cat(Mammal):
    def meow(self):
        print('meow')


perro = Dog()
gato = Cat()

perro.walk()
perro.bark()
gato.walk()
gato.meow()
