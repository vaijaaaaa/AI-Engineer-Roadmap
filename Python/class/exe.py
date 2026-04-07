class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

obj = Person("John smith")
print(obj.name)
obj.talk()


obj2 = Person("Bob Simth")
obj2.talk()