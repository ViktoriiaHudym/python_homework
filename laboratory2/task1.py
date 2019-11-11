"""
Вивести всі квадрати натуральних чисел, які не перевищують числа N.
"""
import re
re_integer = re.compile('^[+-]{0,1}\d+$')

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def int_number(promt):
    number = int(validator(re_integer, promt))
    return number

def main():
    n = 1
    while n**p<=N:
        print(n**p)
        n+=1

N = int_number('Введіть N (обмеження): ')
p = int_number('Числа якого степеня необхідно вивести? ')

print(main())