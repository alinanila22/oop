"""
dander методы
методические методы
"""
class Animal:
    color = "green"
    def __init__(self, paws: int = 4):
        print("Вызов __init__")
        self.paws = paws

    def __del__(self):
        print("Удаление экземпляра класса:", self)

animal = Animal()
# del animal
print("Заверщение программы")
# print(animal.__dict__)