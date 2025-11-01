# """
# ======================================
# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.

class Cat:
    def speak(self):
        return "Мяу!"
class Dog:
    def speak(self):
        return "Гав!"
class Duck:
    def speak(self):
        return "Кря!"

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.speak())

# # Результат:
# # Мяу!
# # Гав!
# # Кря!

# ======================================
# 2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого.

class Shape:
    pass
class Square(Shape):
    def get_pr(self):
        return "Квадрат"
class Rectangle(Shape):
    def get_pr(self):
        return "Прямоугольник"
class Triangle(Shape):
    def get_pr(self):
        return "Треугольник"

shapes = [Square(), Rectangle(), Triangle()]

for A in shapes:
    print(A.get_pr())

# Результат:
# Квадрат
# Прямоугольник
# Треугольник

# ======================================
# 3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

shapes = Shape()
# TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'get_pr'

# ======================================
# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.

class A:
    def __init__(self):
        print("init A")
        super().__init__()

class B:
    def __init__(self):
        print("init B")
        super().__init__()

class C:
    def __init__(self):
        print("init C")
        super().__init__()

class D(A,B,C):
    def __init__(self):
        print("init D")
        super().__init__()

d = D()

print(D.__mro__)

# Результат:
# init D
# init A
# init B
# init C
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)

# ======================================
# 5. Создай MixinLog (как в уроке).
# Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# Создай класс, который наследует оба класса. Создай экземпляр этого класса.

class MixinLog:
    def log(self, message):
        print(f'[LOG]: {message}')

class HotelBook(MixinLog):
    def __init__(self, guest_name, guest_phone, room_number, night_day, price):
        self.guest_name = guest_name
        self.guest_phone = guest_phone
        self.room_number = room_number
        self.night_day = night_day
        self.price = price
        self.is_booked = False

    def total_price(self):
        return self.night_day * self.price
    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return f'Номер {self.room_number} забронирован для {self.guest_name}'
        return "Уже забронирован"

    def cancel(self):
        if self.is_booked:
            self.is_booked = False
            return f"Бронирование для {self.guest_name} отменено"
        return "Активного бронирования нет"

class LoggableHotelBook(HotelBook, MixinLog):
    def __init__(self, guest_name, guest_phone, room_number, night_day, price):
        super().__init__(guest_name, guest_phone, room_number, night_day, price)
        self.log(f"Создана бронь: {guest_name}")

    def book(self):
        result = super().book()
        self.log(result)
        return result
    def cancel(self):
        result = super().cancel()
        self.log(result)
        return result

booking = LoggableHotelBook("Нелли Клинова", "+79265562525", 301, 5, 10000)
print(booking.book())
print(booking.cancel())
print(f"Общая стоимость: {booking.total_price()} руб.")

# Результат:
# [LOG]: Создана бронь: Нелли Клинова
# [LOG]: Номер 301 забронирован для Нелли Клинова
# Номер 301 забронирован для Нелли Клинова
# [LOG]: Бронирование для Нелли Клинова отменено
# Бронирование для Нелли Клинова отменено
# Общая стоимость: 50000 руб.

# ======================================
# 6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?

class Goods:
    def print_info(self):
        print("Вызван метод из Goods")

class MixinLog:
    def print_info(self):
        print("Логирование: метод MixinLog")

class NoteBook(Goods, MixinLog):
    pass

laptop = NoteBook()
laptop.print_info()
print(NoteBook.__mro__)

class NoteBookAlt(MixinLog, Goods):
    pass

pc = NoteBookAlt()
pc.print_info()
print(NoteBookAlt.__mro__)

# ======================================
# ======================================
# Далее задания можете сделать через классы, функции или без них.
# ======================================
# ======================================
# 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"

x = int(input("Введите делимое: "))
y = int(input("Введите делитель: "))

try:
    result = x / y
    print("Частное:", result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите целые числа")

# ======================================
# 8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"

try:
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))

    result = x / y
    print("Частное:", result)

except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")

# ======================================
# 9. Модифицируй код так, чтобы после обработки конкретных ошибок
# был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# "Произошла неизвестная ошибка"

try:
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))

    result = x / y
    print("Частное:", result)

except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")
except Exception:
    print("Произошла неизвестная ошибка")

# ======================================
# 10. При перехвате исключений из 7 и 8 заданий,
# сохрани ошибку в переменную e и выведи её текст:

try:
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))

    result = x / y
    print("Частное:", result)

except ZeroDivisionError as e:
    print("На ноль делить нельзя!")
    print(f"Текст ошибки: {e}")
except ValueError as e:
    print("Ошибка ввода: введите два числа через пробел")
    print(f"Текст ошибки: {e}")

# ======================================
# 11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.

try:
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))
    print(x / y)

except ArithmeticError:
    print("Нельзя делить на ноль")
except ValueError:
    print("Нужно вводить только числа")

# ======================================
# 12. Запроси у пользователя два числа и выполни деление.
# Если деление прошло успешно без ошибок — выведи
# "Деление выполнено успешно" через (но не в блоке try)

try:
    x, y = int(input("Введите первое число: ")), int(input("Введите второе число: "))
    print(f"Результат: {x / y}")
except ArithmeticError:
    print("На ноль делить нельзя!")
else:
    print("Деление выполнено успешно")

# ======================================
# 13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления.

try:
    x, y = int(input("Введите первое число: ")), int(input("Введите второе число: "))
    print(f"Результат: {x / y}")
except ArithmeticError:
    print("На ноль делить нельзя!")
else:
    print("Деление выполнено успешно")
finally:
    print("Работа программы завершена")

# ======================================
# 14. Реализуй две вложенные конструкции:
# Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
# Внутренний try/except ловит деление на ноль.

try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))

    try:
        result = x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

except ValueError:
    print("Ошибка ввода: введите числа")

# ======================================
# 15. Вынеси обработку деления в отдельную функцию divide(x, y)
# с собственным try/except.
# Во внешнем коде обработай только ошибку ввода.

def divide(x, y):
    try:
        print = x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    divide(x, y)

except ValueError:
    print("Ошибка ввода: введите числа")

# """