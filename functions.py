# -*- coding: utf-8 -*-

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script, hours, per_hour, bonus = argv
try:
    salary = float(hours) * float(per_hour) + float(bonus)
except ValueError:
    salary = 'no data'
print(salary)