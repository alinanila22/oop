# """
# ======================================
# 1. Создай класс Circle, в котором:
# есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
# метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
# Проверь результат вызова:
# print(Circle.is_valid_radius(500))   # True
# print(Circle.is_valid_radius(1500))  # False

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

# Проверка
print(Circle.is_valid_radius(500))  # True
print(Circle.is_valid_radius(1500)) # False

# ======================================
# 2. Добавь в класс Circle:
# статический метод area(radius),
# который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
# инициализацию в __init__, которая сохраняет радиус,
# только если он проходит валидацию через метод is_valid_radius()
# (подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
# Пример:
# c = Circle(10)
# print(c.area(c.radius))  # Площадь круга

import math

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return math.pi * radius ** 2

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius
        else:
            self.radius = None

# Пример:
c = Circle(10)
print(f"Площадь круга: {c.area(c.radius)}")  # Площадь круга: 314.1592653589793

# ======================================
# 3. Расширь Circle, добавив обычный метод print_info, который выводит:
# Радиус: ...
# Допустимый диапазон: [MIN, MAX]
# Метод должен использовать и self, и атрибуты класса через type(self).
#
# Пример вызова:
# c.print_info()

import math

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return math.pi * radius ** 2

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius
        else:
            self.radius = None
    def print_info(self):
        print(f'Радиус: {self.radius}')
        print(f'Допустимый диапазон: [{type(self).MIN_RADIUS}, {type(self).MAX_RADIUS}]')

c = Circle(5)
c.print_info()

# Пример
# Радиус: 5
# Допустимый диапазон: [1, 1000]

# ======================================
# 4. Создай класс User, в котором:
#
# приватные атрибуты __login и __password;
# метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
# метод get_credentials(), который возвращает кортеж из логина и пароля.
# Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.

class User:
    def __init__(self):
        self._login = None
        self._password = None

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self._login = login
            self._password = password
    def get_credentials(self):
        return (self._login, self._password)

# Проверка приватности
user = User()
user.set_credentials('login', 'password')
print(user.get_credentials())

# Прямое изменение не работает
user.__login = "attacker"
print(user.get_credentials()) # остались старые данные: ('login', 'password')

# ======================================
# 5. Добавь в User:
#
# метод check_password(password) — возвращает True,
# если переданное значение совпадает с сохранённым паролем;
# приватный метод __encrypt_password(password),
# который возвращает пароль в верхнем регистре (имитация шифрования);
# в set_credentials вызывай __encrypt_password.
# Пример:
# u = User()
# u.set_credentials("daniil", "qwerty")
# print(u.check_password("qwerty"))      # True
# print(u.check_password("qwe"))         # False

class User:
    def __init__(self):
        self._login = None
        self._password = None
    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self._login = login
            self._password = self.__encrypt_password(password)
    def get_credentials(self):
        return (self._login, self._password)

    def check_password(self, password):
        return (self.__encrypt_password(password) == self._password)

# Проверка
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False

# ======================================
# 6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
# Попробуй это сделать — и поясни результат.
# Также выведи напрямую u.__password — и проверь, что будет ошибка.
#
# Попробуй добраться до данных через u._User__password

class User:
    def __init__(self):
        self._login = None
        self._password = None
    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self._login = login
            self._password = self.__encrypt_password(password)
    def get_credentials(self):
        return (self._login, self._password)

    def check_password(self, password):
        return (self.__encrypt_password(password) == self._password)


u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty")) # True
print(u.check_password("qwe")) # False


# Приватный метод Нельзя вызвать извне
# print(u.__encrypt_password("56465"))  # AttributeError(Ошибка!)

# Попытка напрямую получить приватный атрибут __password Нельзя
# print(u.__password)  # AttributeError(Ошибка!)

# Можно добраться до данных через имя с классом
print(u._User__password)  # QWERTY
