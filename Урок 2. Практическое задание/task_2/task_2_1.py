"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
NUMB = int(input('Ведите натуральное число: '))
EVEN = 0
ODD = 0
START_NUMB = NUMB
COUNT = 0
if NUMB != 0:
    while NUMB > 0:
        if NUMB % 2 == 0:
            EVEN += 1
            NUMB = NUMB // 10
            COUNT += 1
        else:
            ODD += 1
            NUMB = NUMB // 10
            COUNT += 1
    print(f'В числе {START_NUMB} всего цифр - {COUNT}, из которых {EVEN} четных и {ODD} нечетных')
else:
    print('Введено число неудовлетворяющее условию')