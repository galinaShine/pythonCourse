# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

new_list = [2, 'example', True, None, ['1'], (4, 234, 45.8, "text", "word", "el", True, None),
{'key_1': 'val_1', 'key_2': 'val_2'}]
for el in new_list:
    print(type(el))
    if type(el) is tuple:
        print(f'found tuple! {el}')
print(new_list)

new_el = input('enter new el for the lest:')
new_list.append(new_el)
index = new_list.index(new_el)
print(type(new_list[index]))


# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

test_list = list(input('enter str for a list'))
print(test_list)
print(len(test_list) // 2)
index = 0
for i in range(len(test_list) // 2):
    test_list[index], test_list[index + 1] = test_list[index + 1], test_list[index]
    index +=2
print(test_list)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month_dict = {
    1: ['January', 'winter'],
    2: ['Fabruary', 'winter'],
    3: ['March', 'spring'],
    4: ['April', 'spring'],
    5: ['May', 'spring'],
    6: ['June', 'summer'],
    7: ['July', 'summer'],
    8: ['August', 'summer'],
    9: ['September', 'autumn'],
    10: ['October', 'autumn'],
    11: ['November', 'autumn'],
    12: ['December', 'winter']
}
numb = int(input('enter month number:'))
if numb <= 0 or numb > 12:
    print('wrong data')
else:
    month_season = month_dict.get(numb)
    print(f'Your number is {numb}, your month is {month_season[0]}, it is {month_season[1]}')


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

input_list = input('enter several words:').split(' ')
if len(input_list) < 2:
    print('told u - several')
else:
    res_list = []
    for el in input_list:
        if el != '':
            res_list.append(el)
    if len(res_list) < 1:
        print('words, not spaces')
    else:
        for i in range(len(res_list)):
            print(f'{i+1}. {res_list[i][:10]}')
        for ind, el in enumerate(res_list): ### или через enumerate
            print(f'{ind + 1}. {el[:10]}')

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

numb_list = [7, 5, 3, 3, 2]
new_list = numb_list.copy()
new_el = int(input('enter your number:'))
for ind, el in enumerate(numb_list):
    if new_el > el:
        new_list.insert(ind, new_el)
        break
else: ### если цикл отработал до конца без брейка
    new_list.append(new_el)
print(new_list)


# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: © geekbrains.ru 38 название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — значений-характеристик, например, список названий товаров.
# Пример: {
# “название”: [“компьютер”, “принтер”, “сканер”], “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”] }


### заготовка, чтобы не заполнять всю структуру руками
animal_list = [
    (1, {'name': 'dog', 'price': 5, 'number': 10, 'unit': 'ind.'}),
    (2, {'name': 'cat', 'price': 7, 'number': 5, 'unit': 'ind.'}),
    (3, {'name': 'rat', 'price': 3, 'number': 15, 'unit': 'ind.'}),
    (4, {'name': 'parrot', 'price': 17, 'number': 3, 'unit': 'ind.'}),
    (5, {'name': 'rabbit', 'price': 8, 'number': 6, 'unit': 'ind.'}),
]
while True:
    new_name = input('enter new animal:')
    new_price = float(input('how much?'))
    new_numb = int(input('how many?'))
    new_unit = input('enter unit:')
    new_item = (len(animal_list) + 1, dict(name = new_name, price = new_price, number = new_numb, unit = new_unit))
    animal_list.append(new_item)
    ans = input('enough? type y/n')
    if ans == 'y':
        break
print(animal_list)

animal_dict = {}
all_keys = animal_list[0][1].keys()
for el in all_keys:
    animal_dict.update({el : set()}) ### используем множество, чтобы избавиться от дублей

for el in animal_list:
    for item in el[1]:
        animal_dict[item].add(el[1].get(item))

for el in animal_dict: ### доп цикл, если выводить все же хотим не множество, а список
    animal_dict[el] = list(animal_dict[el])

from pprint import pprint
pprint(animal_dict)