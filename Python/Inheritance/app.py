class Mammal:
    def walk(self):
        print("Walking")

    
class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

dog = Dog()
dog.walk()

cat = Cat()
cat.walk() 