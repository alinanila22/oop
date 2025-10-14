# """
# ++++++++++++++++++++++++++++++++++++++
# Классы и атрибуты
# ++++++++++++++++++++++++++++++++++++++
# ======================================
# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.

# class Dog:
#     species = "canis"
#     legs = 4

# dog1 = Dog()
# dog2 = Dog()

# print(dog1.__dict__)
# print(dog2.__dict__)

# Пример:
# canis
# canis

# dog1.species = "yorkshire terrier"
# print(dog1.species)
# print(dog2.species)

# Пример:
# yorkshire terrier
# canis

# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.

# class Dog:
#     '''
#     Класс для создания собак с характеристиками
#     '''
#     species = "canis"
#     legs = 4
#
# print(Dog.__doc__) # Класс для создания собак с характеристиками
#
# my_dog = Dog()
# setattr(my_dog, 'name', 'Юджина')
# setattr(my_dog, 'age', 2)
#
# print(getattr(my_dog, 'name'))
# print(getattr(my_dog, 'age'))
#
# delattr(my_dog, 'name')
# print(my_dog.name)

# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.

class User:
    role = "guest"
    active = True

# setattr(User, "role", 'admin')
# print(User.role)

# print(getattr(User, "active"))

# setattr(User, "email", 'abc3"gmail.com')
# print(User.email)

delattr(User, "role")
print(User.__dict__)

# """