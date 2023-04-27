class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def description(self):
        print(f"{str(self.name)} {str(self.age)}")