"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
NUMB_USER = int(input('Введите натуральное число: '))
RESULT = 0
while NUMB_USER > 0:
    RESULT = NUMB_USER % 10 + RESULT * 10
    NUMB_USER = NUMB_USER // 10
print(f'Исходное число - {NUMB_USER}, перевернутое число - {RESULT}')