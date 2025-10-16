# """
# ======================================
# 1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
# Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
# Создай два объекта и задай им разные значения. Выведи информацию по каждому.

# class Person:
#     def set_data(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_date(self):
#         return f"Имя: {self.name}, Возраст: {self.age}"
# person1 = Person()
# person1.set_data("Кирилл", 30)
#
# person2 = Person()
# person2.set_data("Kate", 38)
#
# print(person1.get_date())
# print(person2.get_date())

# Результат:
# Имя: Кирилл, Возраст: 30
# Имя: Kate, Возраст: 38
# ======================================
# 2. Добавь в класс Point методы set_coords(x, y) и get_coords().
# Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
# После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().

# class Point:
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coords(self):
#         return (self.x, self.y)
#
# p = Point()
#
# p.set_coords(7, 12)
# print(f"Координаты: {p.get_coords()}")
#
# # Координаты: (7, 12)
#
# p.set_coords(-3, 5)
# print(f"Другие координаты: {p.get_coords()}")

# Другие координаты: (-3, 5)
# ======================================
# 3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
# # Проверь, что результат совпадает с обычным вызовом p.get_coords().

# class Point:
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coords(self):
#         return (self.x, self.y)
#
# p = Point()
#
# p.set_coords(7, 12)
#
# print(f"Обычный вызов: {p.get_coords()}")
# Обычный вызов: (7, 12)
#
# method = getattr(p, 'get_coords')
# print(method())
# (7, 12)
#
# print(p.get_coords() == method())
# True
# ======================================
# 4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
# Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Имя: {self.name}, возраст: {self.age}")
#
# person = Person("Кирилл", 38)
# person.show_info()
#
# # Рузультат:
# # Имя: Кирилл, возраст: 38
# ======================================
# 5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
# где <имя> — значение поля name. Создай и удали объект вручную с помощью del.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Создан объект: {self.name}")
#
#     def __del__(self):
#         print(f"Удалён объект: {self.name}")
#
#     def show_info(self):
#         print(f"Имя: {self.name}, возраст: {self.age}")
#
#
# person = Person("Kate", 38)
# person.show_info()
#
# print("Сейчас удалим объект...")
# del person
# print("Объект удалён!")
# ======================================
# 6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
# Добавь метод area(), который возвращает площадь прямоугольника.
# Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.

# class Rectangle:
#     def __init__(self, width = 1, height = 1):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# print(f"Прямоугольник (1X1): площадь = {Rectangle().area()}") # без аргументов
# print(f"Прямоугольник (2X5): площадь = {Rectangle(2, 5).area()}") # с заданной шириной и высотой

# Результат:
# Прямоугольник (1X1): площадь = 1
# Прямоугольник (2X5): площадь = 10
# ======================================
# 7. Создай класс Logger, который всегда возвращает один и тот же объект.
# При создании экземпляра в __new__ выводи Создание логгера,
# а при вызове __init__ — Инициализация логгера.

# class Logger:
#     instance = None
#     def __new__(cls):
#         if cls.instance is None:
#             print("Создание логгера")
#             cls.instance = super().__new__(cls)
#         return cls.instance
#     def __init__(self):
#         print("Инициализация логгера")
#
# logger1 = Logger()
# logger2 = Logger()
#
# print(id(logger1))
# print(id(logger2))
# # print(logger1 == logger2)
# print(logger2 is logger1)
# ======================================
# """