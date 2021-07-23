"""Импорт всех задач из Calculator """
from Calculator import Calculator1
import random

"""Лист рандома из 100 чисел выделено 20 случайных чисел"""

def rand_list() :
    rand_list = []
    while len(rand_list) < 20:

        r = random.randint(0, 100)
        if r not in rand_list :
            rand_list.append(r)
    return rand_list

"""Вывод одного числа из 20 случайных  чисел"""

rand1 = random.choice(list(rand_list()))
rand2 = random.choice(list(rand_list()))
# print(rand_list())

"""Инициализация класса"""
class Calculator(Calculator1):
    def divisions(*val1, **val2):
        print(Calculator1.divisions(val1, val2))
        pass
    def add(*val1, **val2):
       print(Calculator1.add(val1, val2))
       pass
    def mul(*val1, **val2):
       print(Calculator1.mul(val1, val2))
       pass
    def minus(*val1, **val2):
       print(Calculator1.minus(val1, val2))
       pass


"""Показ всех операции из обьекта класса """

print(Calculator1.divisions(val1=rand1, val2=rand2))
print(Calculator1.add(val1=rand1, val2=rand2))
print(Calculator1.mul(val1=rand1, val2=rand2))
print(Calculator1.minus(val1=rand1, val2=rand2))


"""Бесконечное значение и калькуляция любых цифр"""

print(Calculator1.add(5, 51, 5, 15, 5, 15, 1, 51, 5, 15, 1, 5))
print(Calculator1.divisions(1, 51, 5, 15, 5, 15, 1, 51, 5, 15, 1, 5))
print(Calculator1.minus(11, 51, 5, 15, 5, 15, 1, 51, 5, 15, 1, 5))
print(Calculator1.mul(21, 51, 5, 15, 5, 15, 1, 51, 5, 15, 1, 5))



