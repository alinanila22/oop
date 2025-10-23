# """
# ======================================
# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == "__secret":
            raise ValueError
        return object.__getattribute__(self, name)

    def get_secret(self):
        return self.__secret

data = SecureData("пароль123")
# print(data.__secret)
print(data.get_secret())
# ======================================
# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает

class SecureData:
    def __init__(self, secret):
        self.__secret = secret
    def __getattribute__(self, name):
        if name == "__secret":
            raise ValueError
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "token":
            raise AttributeError("Ошибка")
        super().__setattr__(name, value)

    def get_secret(self):
        return self.__secret

# date.token = "abc123"
date = SecureData("пароль123")
print(date.get_secret())

date.other = "ok"
print(date.other)
# ======================================
# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"

class SafeDict:

    def __getattr__(self, name):
        return   "N/A"

    def __delattr__(self, name):
        print(f"Удалён атрибут {name}")
        super().__delattr__(name)

d = SafeDict()
print(d.unknown)
d.key = 10
del d.key
# ======================================
# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Зарплата должна быть положительным числом!")
        self.__salary = value

e = Employee("Daniil", 5000)
print(e.salary)
e.salary = 8000
print(e.salary)
# e.salary = -100
# ======================================
# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:
#
# del e.salary
# print(e.__dict__)  # salary нет

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError("Зарплата должна быть > 0")
        self.__salary = value

    @salary.deleter
    def salary(self):
        print("зарплата удалена")
        del self.__salary

e = Employee("Daniil", 5000)
del e.salary
print(e.__dict__)

# ======================================
# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

class LoginForm:
    def __init__(self):
        self._username = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        print("username изменён")
        self._username = value
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # admin

# ======================================
# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.

import datetime

class Card:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return f"**** **** **** {self.__number[-4:]}"

    @number.setter
    def number(self, value):
        if not (isinstance(value, str) and value.isdigit() and len(value) == 16):
            raise ValueError("Номер должен быть 16 цифр")
        self.__number = value

    @number.deleter
    def number(self):
        print(f"Удален в {datetime.datetime.now().strftime('%H:%M:%S')}")
        del self.__number


# Тесты
card = Card("1234567890123456")
assert card.number == "**** **** **** 3456"

# card.number = "123"
# del card.number

# ======================================
# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.

class UserData:
    def __init__(self,
                 email: str,
                 age: int,
                is_active: bool

    ):
        self.email = email
        self.age = age
        self.is_active = is_active

    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active,
        }

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
             raise ValueError ("email должен содержать @")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int)) and value >=18:
            raise ValueError ("Возраст должен быть ≥ 18")
        self._age = value

user = UserData("test@mail.com", 35, True)
data = user.json
assert data['email'] == "test@mail.com"
# assert data['age'] == 17 , "Возраст должен быть ≥ 18"
assert data['is_active'] is True
# assert data['email'] == "test-mail", "email должен содержать @"
assert user.json
print(user.json,"Структура корректная")
# """

