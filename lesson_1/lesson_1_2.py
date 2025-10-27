class Animal:
    "Класс для создания животных"
    color = 'green'
    paws = 4

print(Animal.__doc__)
# Пример:
# Класс для создания животных

cat = Animal()
dog = Animal()

# cat.meal = "wiskas"

# print(cat.__dict__)

# Пример:
# {'meal': 'wiskas'}

# setattr(cat, 'meal', 'wiskas')
# print(cat.__dict__)

# Пример:
# {'meal': 'wiskas'}

# setattr(Animal, 'meal', 'wiskas')
# print(Animal.__dict__)

# Пример:
# {'__module__': '__main__', '__firstlineno__': 1, 'color': 'green', 'paws': 4, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Animal' objects>, '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None, 'meal': 'wiskas'}

setattr(cat, 'meal', 'wiskas')
print(cat.meal)

# Пример:
# wiskas

print(cat.meal)
print(getattr(cat, 'meal'))

# Пример:
# wiskas

print(getattr(cat, 'color'))

# Пример:
# green

print(getattr(cat, 'color_paw', '0'))

# Пример:
# 0


# del cat.meal
# print(getattr(cat, 'color_paw', 'атрибут не найден'))

# Пример:
# атрибут не найден

delattr(cat, 'meal')
print(getattr(cat, 'meal', 'атрибут не найден'))

# Пример:
# атрибут не найден