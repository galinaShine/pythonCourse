# для тренировки
import time


class MyAuto:
    # colour = ["white", "silver"]
    # make = "BMW"
    year = 1995
    # name = 'Ann'
    count = 0

    def __init__(self, c, n):
        self.name = n
        self.colour = c
        print(f'hey, {self.name}!')
        MyAuto.count += 1

    def go(self):
        print(f'the colour: {self.colour[0]}, {self.colour[1]}, the name: {self.name}')
        self.year_print()

    def year_print(self):
        print(self.year)


car_1 = MyAuto(["white", "silver"], 'Ann')
car_1.go()
print(car_1.count)


car_2 = MyAuto(["black", "yellow"], 'Tom')
car_1.go()
print(car_2.count)

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from colorama import Fore
from colorama import Style

class TrafficLight:
    colours = ['red', 'yellow', 'green']

    def __init__(self):
        self.__colour = None

    def running(self, c):
        if c not in self.colours or (self.__colour and self.__colour != c):
            print('error')
            return
        ind = self.colours.index(c)
        print(Fore.RED + c if c == 'red' else Fore.GREEN + c if c == 'green' else Fore.YELLOW + c)
        print(Style.RESET_ALL)
        wait_time = 2 if ind % 2 > 0 else 7
        time.sleep(wait_time)
        self.__colour = self.colours[(ind + 1) % 3]

test_light = TrafficLight()
test_light.running('red')
test_light.running('yellow')
test_light.running('green')


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calculate(self, mass_per_km, cm):
        mass = self._length * self._width * mass_per_km * cm / 1000
        print(mass)

road_1 = Road(float(input('enter the length: ')), float(input('enter the width: ')))
road_1.calculate(float(input('enter the mass per m2: ')), float(input('enter the cm: ')))


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": int(w), "bonus": int(b)}

    def print_all(self):
        print(self.name, self.surname, self.position, self._income)


class Position(Worker):
    def __init__(self, n, s, p, w, b):
        super().__init__(n, s, p, w, b)

    def get_full_name(self):
        print(f'full name: {self.name} {self.surname}')

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        print(f'full income: {income}')


worker_1 = Position('Ivan', 'Urgant', 'TV Host', '123', '456')
worker_2.get_full_name()
worker_3.get_total_income()
worker_4.print_all()



# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random

direction = ['left', 'right']
class Car:
    def __init__(self, s, c, n, p):
        self.speed = float(s)
        self.colour = c
        self.name = n
        self.is_police = bool(p)

    def go(self):
        print('start going')

    def stop(self):
        print('stop going')

    def turn(self, direction):
        print(f'the car turned {direction}')

    def turn_random(self):
        self.direction = random.choice(direction)
        print(f'the car turned {self.direction}')

    def show_speed(self):
        print(f'the speed is {self.speed}')


class TownCar(Car):

    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)
        if self.is_police:
            print('wrong type')

    def show_speed(self):
        print(f'the speed is {self.speed}, speed limit!') if self.speed > 60 else print(f'the speed is {self.speed}')

class SportCar(Car):

    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)
        if self.is_police:
            print('wrong type')

class WorkCar(Car):

    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)
        if self.is_police:
            print('wrong type')

    def show_speed(self):
        print(f'the speed is {self.speed}, speed limit!') if self.speed > 40 else print(f'the speed is {self.speed}')

class PoliceCar(Car):

    def __init__(self, s, c, n, p = True):
        super().__init__(s, c, n, p)
        if self.is_police != True:
            print('wrong type')


my_car = PoliceCar(30, 'red', 'BMW', True)
print(my_car.is_police)
my_car = PoliceCar(30, 'red', 'BMW', 0)

my_car_2 = WorkCar(40, 'red', 'BMW', 5)
my_car_2.turn('left')
my_car_2.show_speed()

my_car_3 = TownCar(30, 'red', 'BMW', True)
my_car_3.stop()

my_car_4 = SportCar(30, 'red', 'BMW', False)
my_car_4.go()
my_car_4.turn_random()



# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print('start drawing')


class Pen(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print('drawing with a pen')


class Pencil(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print('drawing with a pencil')


class Handle(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print('drawing with a handle')


pen_drawing = Pen('title 1')
pen_drawing.draw()

pencil_drawing = Pencil('title 1')
pencil_drawing.draw()

handle_drawing = Handle('title 1')
handle_drawing.draw()