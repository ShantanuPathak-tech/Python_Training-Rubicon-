# class Animal():
#     def eat(self):
#         print("Animal is Eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
# d = Dog()
# d.eat()
# d.bark()

# class Animal:
#     def sound(self):
#         print("Animal Sound");
# class Dog(Animal):
#     def sound(self):
#         print("Bark");
# class Cat(Animal):
#     def sound(self):
#         print("Meow");
# animals = {Dog(), Cat()};
# for animal in animals:
#     animal.sound();

class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        print(self._balance)
account = Account(5000)
print(account.get_balance())

