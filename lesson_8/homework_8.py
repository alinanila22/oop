# ======================================
# 1. Создай две функции: inner() и outer().
# В inner() вызови деление на ноль.
# В outer() просто вызови inner().
# Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.

# def inner():
#     result = 5 / 0
#     return result
#
# def outer():
#     return inner()
#
# outer()

# ======================================
# 2. Добавь вокруг вызова outer() конструкцию try/except,
# чтобы перехватить исключение и вывести сообщение
# "Ошибка перехвачена на верхнем уровне".

# def inner():
#     result = 5 / 0
#     return result
#
# def outer():
#     return inner()
#
# try:
#     outer()
#
# except ZeroDivisionError:
#     print("Обнаружено деление на ноль!")

# ======================================
# 3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
# В случае ошибки возвращай строку "Ошибка в inner".

# def inner():
#     try:
#         result = 5 / 0
#         return result
#     except ZeroDivisionError:
#         return "Ошибка в inner"
#
# def outer():
#     return inner()
#
# result = outer()
# print(result)

# ======================================
# 4. Сделай так:
# В inner() ошибка не перехватывается.
# В outer() ошибка перехватывается через try/except.
# В outer() при перехвате напечатай "Ошибка в outer".

# def inner():
#     return 5 / 0
#
# def outer():
#     try:                   # Ошибка перехватывается здесь
#         return inner()
#     except ZeroDivisionError:
#         print("Ошибка в outer")
#
# result = outer()

# ======================================
# 5. Напиши функцию get_value(), которая кидает ValueError.
# Напиши тестовую функцию test_get_value(), которая:
#
# Вызывает get_value();
# Ловит ValueError;
# Завершает тест с assert False, если исключение поймано.

# def  get_value():
#     raise ValueError("Неверное значение")
#
# def test_get_value():
#     try:
#         get_value()
#     except ValueError:
#         assert False, "Тест не должен перехватывать ValueError"
#
# test_get_value()

# ======================================
# ======================================
# 6. Создай функцию divide(x, y).
# Если y == 0, выбрасывай ZeroDivisionError через raise.
# Иначе возвращай результат деления.

# def divide(x, y):
#     if  y == 0:
#         raise ZeroDivisionError("Деление на ноль!")
#     else:
#         return x/y
#
# print(divide(2,3))
# print(divide(10, 0))

# ======================================
# 7. Создай функцию sqrt(x), которая:
# Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
# Иначе возвращает квадратный корень из x.
# Проверь поведение функции через try/except.

# class NegativeNumberError(Exception):
#     pass
#
# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError('Недопустимое отрицательное значение')
#     else:
#         return x ** 0.5
#
# test_values = [16, -9, 6, 2, -7]
# for x in test_values:
#     try:
#         result = sqrt(x)
#         print(f"sqrt({x}) = {result}")
#     except NegativeNumberError as e:
#         print(f"{e}")

# ======================================
# 8. Создай базовый класс MathError.
# От него унаследуй:
# NegativeNumberError
# DivisionByZeroError
# В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
# Проверь в try/except обработку ошибок через базовый класс MathError.

# class MathError(Exception):
#     pass
#
# class NegativeNumberError(MathError):
#     pass
#
# class DivisionByZeroError(MathError):
#     pass
#
# def safe_divide(x, y):
#     if y == 0:
#         raise DivisionByZeroError("Деление на ноль невозможно")
#     return x / y
#
# try:
#     print(safe_divide(7, 0))
#     print(safe_divide(6, 2))
# except MathError as e:
#     print("Произошла ошибка вычислений:", e)

# ======================================
# 9. Создай тестовую функцию test_sqrt(), которая:
# вызывает sqrt(x) с отрицательным числом;
# перехватывает NegativeNumberError;
# завершает тест с assert False и сообщением
# "Нельзя брать корень из отрицательного числа".

# def test_sqrt():
#     try:
#         sqrt(-1)
#     except NegativeNumberError:
#         assert False, "Нельзя брать корень из отрицательного числа"
#
# test_sqrt()

# ======================================
# ======================================
# 10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
# Обеспечь закрытие файла через with.

# with open("sample.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# ======================================
# 11. Создай класс BackupList, который:
# делает копию списка при входе в with,
# при выходе сохраняет изменения, если ошибок не было,
# откатывает изменения при ошибке.
# Проверь:
# успешное изменение списка;
# откат при ошибке.

# class BackupList:
#     def __init__(self, lst):
#         self.lst = lst
#         self.backup = None
#
#     def __enter__(self):
#         self.backup = self.lst.copy()
#         return self.lst
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             self.lst[:] = self.backup
#         return not exc_type
#
# numbers = [1, 2, 3]
# with BackupList(numbers) as lst:
#     lst.append(4)
# print(numbers)
#
# numbers = [1, 2, 3]
# try:
#     with BackupList(numbers) as lst:
#         lst.append(4)
#         raise ValueError
# except ValueError:
#     pass
# print(numbers)

# ======================================
# ======================================
# 12. Создай декоратор-класс Timer,
# который измеряет время выполнения функции и выводит результат.

# import time
#
# class Timer:
#     def __init__(self, message):
#         self.message = message
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.message(*args, **kwargs)
#         end = time.time()
#         duration = end - start
#         print(f"{self.message}: {duration:.2f} seconds")
#         return result
#
# @Timer
# def calculate_sum(a, b):
#     time.sleep(0.5)
#     return a + b
#
# result = calculate_sum(10, 15)
# print(result)