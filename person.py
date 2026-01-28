class Person:
    name: str = ""
    age: int = ""

    def __int__(self, name):
        self.name = name


    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age