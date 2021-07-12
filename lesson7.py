# для тренировки
import re


class MyClass:

    def __init__(self, par, par_2):
        self.par = par
        self.par_2 = par_2

    # def __del__(self):
    #     print('deleted')

    def __str__(self):
        return f'par = {self.par}, par_2 = {self.par_2}'

    def __add__(self, other):
        return MyClass(self.par + other.par, self.par_2 + other.par_2)

    def __call__(self, new_par):
        self.par = new_par

one = MyClass('param', 'marap')
two = MyClass('1', '2')
print(one + two)
one(33)
print(one, two)

# del one
# print(one.par)

from abc import ABC, abstractmethod

class MyTestClass(ABC):

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def second(self):
        pass


class Tiger(MyTestClass):

    def first(self):
        pass

    def second(self):
        pass


tiger_1 = Tiger()


class Iterator:
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 10:
            return self.i
        else:
            raise StopIteration

class IterObject:
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return Iterator(self.start)


iterObj = IterObject(5)
for el in iterObj:
    print(el)

for el in iterObj:
    print(el)



class NewClass:
    def __init__(self, fst, scnd):
        self.fst = fst
        self.scnd = scnd

    @property
    def my_method(self):
        return f'got {self.fst} and {self.scnd}'


mc = NewClass('first', 'second')
print(mc.my_method)


class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2021:
            self.__year = 2021
        else:
            self.__year = year

    def get_year(self):
        return f'year = {self.year}'


car = Auto(20333)
print(car.get_year())




class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_wd(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def com_sq(self):
        main_sq = self.square
        for el in self.wd:
            main_sq -= el.square
        return main_sq


room_1 = Room(10, 2 , 3)
print(room_1.square)

room_1.add_wd(2, 2)
print(room_1.com_sq())




# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
        self.width = len(my_list)
        self.height = len(my_list[0])
        for el in my_list:
            if len(el) != self.height:
                raise ValueError('wrong len')

    def __str__(self):
        result = ''
        for row in self.my_list: # [3, -8]
            result += ' '.join(map(str, row)) + '\n'
        return result

    def __add__(self, other):
        if self.width != other.width or self.height != other.height:
            raise ValueError('wrong size')

        new_list = []
        for _ in self.my_list:
            new_list.append([0] * len(self.my_list[0]))

        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                new_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix(new_list)


test_list_1 = Matrix([[0, 2, 1], [3, 2, 1], [0, 12, 1]])
test_list_2 = Matrix([[0, 2, 1], [2, 1, 1], [4, -1, 1]])

print(test_list_1 + test_list_2)




# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
# работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_needed(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = int(size)

    def cloth_needed(self):
        self.__cloth = round(self.__size / 6.5 + 0.5, 3)
        return self.__cloth

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if 3 < size <= 500:
            self.__size = size
        else:
            self.__size = 300


coat_1 = Coat(600)
print(coat_1.cloth_needed())



class Suit(Clothes):

    def __init__(self, height):
        self.height = float(height)

    @property
    def cloth_needed(self):
        self.cloth = round(2 * self.height + 0.3, 3)
        return self.cloth



suit_1 = Suit(100)
print(suit_1.cloth_needed) # с декоратором

suit_1 = Suit(173)
print(suit_1.cloth_needed())



# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
# деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет
# организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, numb):
        self.numb = int(numb)

    def __str__(self):
        return f'{self.numb}'

    def __add__(self, other):
        new_cell = self.numb + other.numb
        return Cell(new_cell)

    def __sub__(self, other):
        if self.numb - other.numb > 0:
            new_cell = self.numb - other.numb
            return Cell(new_cell)
        else:
            raise ValueError('error')

    def __mul__(self, other):
        new_cell = self.numb * other.numb
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = self.numb // other.numb
        return Cell(new_cell)

    def make_order(self, numb_in_row):
        full_rows = self.numb // numb_in_row
        part_row = self.numb % numb_in_row
        for row in range(full_rows):
            print('*' * numb_in_row)
        print('*' * part_row)

cell_1 = Cell(9)
cell_2 = Cell(2)
print(cell_1 / cell_2)
cell_1 = Cell(90)
cell_1.make_order(25)