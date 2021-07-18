# для тренировки

class MyClass:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def my_1(self):
        print('gotya')
        # return MyClass.my_2()
        # return self.my_2()

    @staticmethod
    def my_2(obj):
        return f'{obj.name} and {obj.surname}'


    @classmethod
    def my_3(cls, data):
        n, s = data
        return cls(n, s)
        # print(cls)
        # return MyClass().my_1()

my_list = ['John', 'River']
one = MyClass.my_3(my_list)
print(MyClass.my_2(one))
# one.my_1()
# MyClass().my_1()
# MyClass.my_2()


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} and {self.surname}'


class Teacger(Person):

    def teach(self, subj, *pupils):
        for el in pupils:
            el.take(subj)


class Pupil(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def take(self, subj):
        self.knowledge.append(subj)


class Subject():

    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects



s = Subject('maths', 'PE')
t = Teacger('John', 'Dawns')
print(t)
p = Pupil('Sam', 'Summer')
print(f'{p}')


t.teach(s, p)
print(p.knowledge[0].my_list())



class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt


num = input('Enter your number')

try:
    num = int(num)
    if num < 0:
        raise MyError('wrong format')

except (ValueError, MyError) as err:
    print(err)

else:
    print(num)



# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def str_to_int(cls, date):
        d, m, y = date.split('-')
        d = int(d)
        m = int(m)
        y = int(y)
        cls.is_valid(d, m, y)
        print(f'{d} {m} {y}')

    @staticmethod
    def is_valid(d, m, y):
        try:
            if d < 1 or d > 31 or m < 1 or m > 12 or y > 99:
                raise MyError('wrong format')
        except (ValueError, MyError) as err:
            print(err)
        else:
            print('ok')


my_date = '12-10-12'
one = Date.str_to_int(my_date)



# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt

num = float(input('Enter first number'))
div = float(input('Enter div number'))

try:
    if div == 0:
        raise MyError("that's 0")
    result = num / div

except (ValueError, MyError) as err:
    print(err)

else:
    print(result)



# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class MyError(Exception):

    def __init__(self, text):
        self.text = text

class MyList():

    def __init__(self):
        self.my_list = []

    def __str__(self):
        return f'{self.my_list}'

    def my_append(self, el):
        try:
            self.my_list.append(float(el))
        except ValueError:
            raise MyError('wrong format')

ent_list = MyList()
stop = False

while True:
    try:
        ent_el = input('Enter new el: ')
        ent_list.my_append(ent_el)
    except MyError as err:
        if ent_el == 'stop':
            stop = True
        else:
            print(err)
    if stop:
        print(f"your list: {ent_list}")
        break




# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class MyError(Exception):
    def __init__(self, text):
        self.text = text


goods = [
    (1, {'product_type': 'printer', 'price': 7, 'numb': 10, 'size': 'L', 'ink_colour': 'black'}),
    (2, {'product_type': 'scanner', 'price': 8, 'numb': 1, 'size': 'M', 'speed': 7}),
    (3, {'product_type': 'xerox', 'price': 9, 'numb': 70, 'size': 'S', 'ink': True}),
]

warehouse_goods = {'printer': 0, 'scanner': 0, 'xerox': 0}
department_goods = {
    'office': {'printer': 0, 'scanner': 0, 'xerox': 0},
    'account': {'printer': 0, 'scanner': 0, 'xerox': 0},
    'shop': {'printer': 0, 'scanner': 0, 'xerox': 0}
}


class Warehouse():

    @staticmethod
    def take_goods(stationary):
        if stationary.product_type != 'printer' and stationary.product_type != 'scanner' and stationary.product_type != 'xerox':
            raise MyError('wrong data')
        warehouse_goods[stationary.product_type] = warehouse_goods[stationary.product_type] + stationary.numb
        print(f'{warehouse_goods}')

    @staticmethod
    def to_depart(stationary, department):
        if department != 'office' and department != 'account' and department != 'shop':
            raise MyError('wrong data')
        if stationary.product_type != 'printer' and stationary.product_type != 'scanner' and stationary.product_type != 'xerox':
            raise MyError('wrong data')
        # отправляем в отдел
        department_goods[department][stationary.product_type] = department_goods[department][stationary.product_type] + stationary.numb
        print(f'{department_goods}')
        # удаляем со склада
        warehouse_goods[stationary.product_type] = warehouse_goods[stationary.product_type] - stationary.numb
        print(f'{warehouse_goods}')

class Stationary():

    def __init__(self, numb, price, size, product_type):
        try:
            self.numb = int(numb)
            self.price = float(price)
            self.size = size
            self.product_type = product_type
        except ValueError:
            raise MyError('wrong format')
        if self.numb <= 0 or self.price <= 0:
            raise MyError('negative')


class Printer(Stationary):

    def __init__(self, numb, price, size, ink_colour):
        super().__init__(numb, price, size, product_type='printer')
        self.ink_colour = ink_colour


class Scanner(Stationary):

    def __init__(self, numb, price, size, speed):
        super().__init__(numb, price, size, product_type='scanner')
        try:
            self.speed = float(speed)
        except ValueError:
            raise MyError('wrong format')
        if self.speed <= 0:
            raise MyError('negative')

class Xerox(Stationary):

    def __init__(self, numb, price, size, ink=True):
        super().__init__(numb, price, size, product_type='xerox')
        try:
            self.ink = bool(ink)
        except ValueError:
            raise MyError('wrong format')


try:
    new_printer = Printer(1, 17, 'L', 'black')
    new_scanner = Scanner(13, 17, 'M', 123)
    new_xerox = Xerox(15, 23, 'S')
    scanner_to_office = Scanner(1, 17, 'L', 123)
    xerox_to_shop = Xerox(1, 23, 'S')
    Warehouse.take_goods(new_printer)
    Warehouse.take_goods(new_scanner)
    Warehouse.take_goods(new_xerox)
    Warehouse.to_depart(scanner_to_office, 'office')
    Warehouse.to_depart(xerox_to_shop, 'shop')
except MyError:
    print('wrong format')




# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных
# чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex_Number():

    def __init__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __add__(self, other):
        return Complex_Number((self.part_1 + other.part_1), (self.part_2 + other.part_2))

    def __mul__(self, other):
        return Complex_Number(self.part_1 * other.part_1 - self.part_2 * other.part_2, self.part_1 * other.part_2 + other.part_1 * self.part_2)

    def __str__(self):
        return f'{self.part_1} + {self.part_2}i'


my_numb = Complex_Number(3, 1)
my_numb_2 = Complex_Number(2, -3)
print(my_numb + my_numb_2)
print(my_numb * my_numb_2)