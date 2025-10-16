class Animal:
    color = "green"
    paws = 4

    def set_color(self, color):
        self.color = color
        print("Установка цвета")

    def get_color(self):
        return self.color
animal = Animal()

# print(animal.get_color())
# print(animal.__dict__)
animal.set_color("blue")

# print(animal.get_color())
result = getattr(animal, "get_color")
print(result())
# print(animal.__dict__)