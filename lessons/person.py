class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        print("Человек создан")

class Warrior(Person):
    """Creating class Warrior"""
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    