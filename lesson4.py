# для тренировки

import time
import random

print(time.time())
print(random.random())
import functions

import math

my_list = [10, 25, 30, 45, 50]
print(my_list)
new_list = [el + 2 for el in my_list if el % 2 == 1]
print(new_list)
print(random.randint(0, 10))
from random import randint

print(randint(0, 10))
from random import randrange

print(randrange(20, 30, 8))

generator = (param * param for param in range(5))
for el in generator:
    print(el)
print(next(generator))

from functools import partial
from functools import reduce


def my_func(param_1, param_2):
    return param_1 ** param_2


new_my_func = partial(my_func, 2)
print(new_my_func)
print(new_my_func(4))

# 2. Представлен список чисел. Необходимо вывести§ элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = []
while True:  # ручной ввод
    numb = int(input('enter numb: '))
    my_list.append(numb)
    ans = input('enough? type y/n')
    if ans == 'y':
        break
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] # заданный список
new_list = [el for ind, el in enumerate(my_list) if my_list[ind] > my_list[ind - 1] and ind != 0]
print(new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = []
while True:  # ручной ввод
    numb = int(input('enter numb: '))
    my_list.append(numb)
    ans = input('enough? type y/n')
    if ans == 'y':
        break
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] # заданный список
new_list = [el for ind, el in enumerate(my_list) if my_list.count(el) == 1]
print(new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_func, my_list))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count

start_numb = int(input('enter number to start:'))
max_numb = int(input('enter max number:'))
numbs = (num for num in count(start_numb))    # итератор, генерирующий целые числа, начиная с указанного

# с ручной остановкой
while True:
    print(next(numbs))
    ans = input('enough? type y/n')
    if ans == 'y':
        break

# с использованием max_numb
el = start_numb
while el <= max_numb - 1:
    el = next(numbs)
    print(el)


from itertools import cycle

my_list = [1, 2, True, 'false', [0]]
max_numb = int(input('enter max number of tries:'))
my_list_cycle = (num for num in cycle(my_list))   # итератор, повторяющий элементы некоторого списка, определенного заранее

# с ручной остановкой
while True:
    print(next(my_list_cycle))
    ans = input('enough? type y/n')
    if ans == 'y':
        break

# с использованием max_numb
numb_of_try = 0
while numb_of_try <= max_numb - 1:
    numb_of_try += 1
    print(next(my_list_cycle))

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    fact_numb = 1
    for i in range(1, n + 1):
        fact_numb *= i
        yield fact_numb

numb = int(input('enter numb:'))

for el in fact(numb):
    print(el)