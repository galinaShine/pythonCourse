# Задание 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

startKM = float(input('enter first day run: '))
goalKM = float(input('enter your goal: '))
if startKM <= 0 or goalKM <= 0:
    print('impossible')
elif startKM >= goalKM:
    print('already done that')
else:
    curKM = startKM
    day = 0
    while curKM < goalKM:
        curKM = curKM + curKM/100*10
        day += 1
    print(f'You need {day} day/days to reach {goalKM}km')


# Задание 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

earn = int(input('enter your earnings: '))
exp = int(input('enter your expenses: '))
profit = earn - exp
if profit > 0:
    eff = profit / earn
    print(f'good job! your efficiency is {eff}!')
    staff = int(input('enter number of workers: '))
    if staff <= 0:
        print('how come?')
    else:
        profitPP = profit / staff
        print(f'profit per person is {profitPP}!')
elif profit < 0:
    print('work harder')
else:
    print('OK')

# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('enter a positive number: '))
if number <= 0:
    print('I asked for a positive number')
else:
    biggest_number = 1
    strNumber = str(number)
    while number > 0:
        last_numb = number % 10
        number = number // 10
        if biggest_number >= last_numb:
            continue
        biggest_number = last_numb
    print(biggest_number)

# Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# с отрицательными числами не работает

number = input('enter your number: ')
second_number = number + number
third_number = second_number + number
sum = int(number) + int(second_number) + int(third_number)
print(f'gotya! {number} + {second_number} + {third_number} = {sum}')


# Задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

second_number = number + number
third_number = second_number + number
print(f'the sum of {number} + {second_number} + {third_number} is: ')
print(int(number) + int(second_number) + int(third_number))
seconds = int(input('enter seconds: '))
days = seconds//(24*3600)
hours = seconds%(24*3600)//3600
minutes = seconds%3600//60
rest_seconds = seconds%3600%60
print(f'{days}:{hours}:{minutes}:{rest_seconds}')


# Задание 1
# запросить ввести число, запомнить его, вывести, простейшие операции со строками

number = int(input('enter the 1st number: '))
print(f'1st number: {number}!')

sum = number + int(input("enter the 2nd number: "))
print(f'the sum is {sum}!')

string_1 = input('enter the 1st number (but it will be a string): ')
string_2 = input('enter the 2nd number (but it will be a string as well): ')
print(string_1 + string_2)
