# для тренировки
test = open('text.md', 'a', encoding='utf-8')
test.writelines(['\n- четвертое', '\n- пятое', '\n- шестое'])
print('- седьмое', file=test)
for i in test:
    print(i, end='')
print(test)
test.close()

with open('text.md', 'a', encoding='utf-8') as test:
    print('- восьмое', file=test)
    print(test)

import json

data = {
    'salary': {
        "income" : 234,
        'bonus': 123
    },
    'payment': True
}

with open('new_file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

num_j = json.dumps(data)
print(type(num_j))

with open('new_file.json', 'r', encoding='utf-8') as f:
    num_i = json.load(f)

print(type(num_i))

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

with open('lesson5/task4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)

txt = 'One - 1 Two - 2 Three - 3 Four - 4'
trans_table = str.maketrans({'One': 'Один', 'Two': 'Два', 'Tree': 'Три', 'Four': 'Четыре'})
print(txt.translate(trans_table))

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.



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




# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
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

