# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dev(a, b):
    """
    выполняет деление двух чисел
    :param a: делимое
    :param b: делитель (не может быть 0)
    :return: остаток от деления
    """
    res = "can't do that" if b == 0 else round(a / b, 8)
    return res

while True:
    a = int(input('enter first number:'))
    b = int(input('enter second number:'))
    print(dev(a, b))

# через лямбду, но не поняла как в таком случае предусмотреть 0
print((lambda num_1, num_2: num_1 / num_2)(int(input('enter first number:')), int(input('enter second number:'))))

# через except
def dev_2(a, b):
    try:
        res = a / b
    except ZeroDivisionError as error:
        res = error
    return res

while True:
    a = int(input('enter first number:'))
    b = int(input('enter second number:'))
    print(dev_2(a, b))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def data(name, surname, year, city, email, tel):
    print(f'name: {name}, surname: {surname}, year of birth: {year}, city of living: {city}, email: {email}, phone number: {tel}')

data(
    input('your name:'),
    input('your surname:'),
    int(input('year of birth:')),
    input('city of living:'),
    input('your email:'),
    int(input('your phone number:'))
)

### через kwargs
def data_2(**kwargs):
    """
    выводит полученную информацию одной строкой
    :param kwargs: входные данные о пользователе
    :return: вывод данных о пользователе одной строкой
    """
    res = ''
    for el in kwargs:
        res += f'{el}: {kwargs.get(el)}, '
    print(res[:-2:])

data_2(name = 'Ivan', surname = 'Ivanov', year = 1978, city = 'London', email = 'exp@mail.ru', number = 1234567)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    """
    принимает три позиционных аргумента, возвращает сумму наибольших двух аргументов
    :param num_1: первое число
    :param num_2: второе число
    :param num_3: третье число
    :return: сумма наибольших двух из полученных чисел
    """
    if type(num_1) is not float or type(num_2) is not float or type(num_3) is not float:
        res = 'error'
    else:
        global my_list # для экспериментов
        my_list = list((num_1, num_2, num_3))
        my_list.remove(min(num_1, num_2, num_3))
        res = round(sum(my_list), 2)
    return res

first_numb = float(input('enter 1st number:'))
second_numb = float(input('enter 2nd number:'))
third_numb = float(input('enter 3rd number:'))
print(my_func(first_numb, second_numb, third_numb))
print(my_list) # для экспериментов


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

### через оператор **
def my_func(x, y):
    if (type(x) is int or type(x) is float) and x > 0 and type(y) is int and y < 0:
        res = x ** y
    else:
        res = 'error'
    return res

print(my_func(32, -3))

### через цикл
def my_func_2(x, y):
    if (type(x) is int or type(x) is float) and x > 0 and type(y) is int and y < 0:
        res = 1
        for i in range(abs(y)):
            res *= x
        res = 1 / res
    else:
        res = 'error'
    return res

print(my_func_2(32, -3))



# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.



# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().