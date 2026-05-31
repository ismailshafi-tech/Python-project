class animal:
     def __init__(self, name):
          self.name = name
          self.is_alive = True 

     def eat(self):
          print(f"{self.name} is eating")

     def sleep(self):
          print(f"{self.name} is sleeping")

#class Dog(animal):               
 #    pass
class Dog(animal):
     def speak(self):
          print("dog is speaking")
     

class Cat(animal):
     pass
class Mouse(animal):
     pass

dog = Dog("scooby")
cat = Cat("meow")
mouse = Mouse("mickey")

print(dog.name)
print(cat.name)
print(mouse.name)
cat.eat()
dog.sleep()
dog.speak()