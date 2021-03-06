# для тренировки
# test = open('text.md', 'a', encoding='utf-8')
# test.writelines(['\n- четвертое', '\n- пятое', '\n- шестое'])
# print('- седьмое', file=test)
# for i in test:
#     print(i, end='')
# print(test)
# test.close()
#
# with open('text.md', 'a', encoding='utf-8') as test:
#     print('- восьмое', file=test)
#     print(test)
#
# import json
#
# data = {
#     'salary': {
#         "income" : 234,
#         'bonus': 123
#     },
#     'payment': True
# }
#
# with open('new_file.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f)
#
# num_j = json.dumps(data)
# print(type(num_j))
#
# with open('new_file.json', 'r', encoding='utf-8') as f:
#     num_i = json.load(f)
#
# print(type(num_i))

#######################################################################

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('lesson5/task1.txt', 'w', encoding='utf-8') as f:
    while True:
        new_str = input('enter new string:')
        if new_str != '':
            f.write(f'{new_str}\n')
        else:
            print('the end')
            break


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('lesson5/task2.txt', 'r', encoding='utf-8') as f:
    str_numb = 0
    word_per_str = 0
    for line in f:
        str_numb +=1
        word_number = len(line.split(' ')) if line != '\n' else 0
        print(f'line number: {str_numb}, word number: {word_number}')
print(f'total number of strings: {str_numb}')


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('lesson5/task3.txt', 'a+', encoding='utf-8') as f:
    while True:
        surname = input('enter new surname: ')
        salary = float(input('enter the salary: '))
        print(f'\n{surname} {salary}', file=f, end='')
        enough = input('enough? y/n')
        if enough == 'y':
            break

    f.seek(0)
    less_20 = ''
    worker_numb = 0
    total_salary = 0
    for line in f:
        surname = line.split(' ')[0]
        salary = float(line.split(' ')[1])
        print(f'surname: {surname}, salary: {salary}')
        if salary < 20000:
            less_20 += surname + ', '
        worker_numb += 1
        total_salary += salary
avr_salary = float('{:.3f}'.format(total_salary / worker_numb))
print(f'less than 20 club members: {less_20[:-2:]}')
print(f'average salary: {avr_salary}')



# 4. Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator
translator = Translator(to_lang="Russian")
my_new_file = open('lesson5/test_4.txt', 'a', encoding='utf-8')
with open('lesson5/task4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        new_list = line.split(' ')
        numb = new_list[0]
        rest_line = ' '.join(new_list[1:])
        rus_numb = translator.translate(numb)
        print(' '.join([rus_numb, rest_line]), file=my_new_file, end='')
my_new_file.writelines(['\n'])
my_new_file.close()


################### через функцию генератор

from translate import Translator
translator = Translator(to_lang="Russian")

task4 = open('lesson5/task4.txt', 'r', encoding='utf-8')
test_4 = open('lesson5/test_4.txt', 'a', encoding='utf-8')

def my_func(file):
    for line in file:
        new_list = line.split(' ')
        numb = new_list[0]
        rest_line = ' '.join(new_list[1:])
        rus_numb = translator.translate(numb)
        new_line = ' '.join([rus_numb, rest_line])
        yield new_line

for line in my_func(task4):
    print(line, file=test_4, end='')

test_4.writelines(['\n'])
task4.close()
test_4.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('lesson5/test_5.txt', 'w', encoding='utf-8') as f:
    total = 0
    while True:
        new_numb = input('enter new number:')
        try:
            new_numb = int(new_numb)
            f.write(f'{new_numb} ')
            total += new_numb
            print(f'total sum: {total}')
            enough = input('enough? y/n')
            if enough == 'y':
                print('the end')
                break
        except ValueError:
            print('ValueError')
            break


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


my_dict = {}
with open('lesson5/task6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_content = line.split(' ') # ['Physics:', '70(л)', '20(пр)', '18(лаб)\n']
        subj = line_content[0][:-1]
        total_hours = 0
        for el in line_content[1:]:   # ['70(л)', '20(пр)', '18(лаб)\n']
            el = el.strip()
            if el != '-':           # '70(л)
                ind = el.find('(')
                el = el[:ind]
                total_hours += int(el)
        my_dict[subj] = total_hours
        print(line_content, subj, total_hours)
print(my_dict)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

total_profit = 0
numb_of_comp = 0
my_list = [{}, {}]
with open('lesson5/task7.txt', 'r', encoding='utf-8') as f:
    for line in f: # Brooms ПАО 2500000 500000
        line_content = line.split(' ') # ['Brooms', 'ПАО', '2500000', '500000\n']
        name = line_content[0]
        income = float(line_content[2])
        expen = float(line_content[3].strip()) # ['Brooms', 'ПАО', '2500000', '500000']
        profit = income - expen
        if profit > 0:
            total_profit += profit
            numb_of_comp += 1 # не включала компании с отрицательной прибылью даже в подсчет кол-ва компаний, но может их не надо было включать только в общую сумму прибыли?
        my_list[0][name] = profit
    avr_profit = total_profit / numb_of_comp
    my_list[1]['average_profit'] = avr_profit
import json
with open("lesson5/task7.json", "w", encoding='utf-8') as f:
    json.dump(my_list, f, ensure_ascii=False, indent=4)