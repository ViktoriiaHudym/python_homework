"""
Увести з клавіатури цілі числа a, b.
Якщо числа не рівні, то замінити кожне з них одним і тим же числом, рівним більшому із вихідних,
а якщо рівні, то замінити числа нулями.
"""
import re
re_integer = re.compile('^[+-]{0,1}\d+$')

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def int_number(promt):
    number = int(validator(re_integer,promt))
    return number

def main():
    if a > b:
        return (a, a)
    elif b > a:
        return (b, b)
    else:
        return (0, 0)

a = int_number('Введіть ціле число a: ')
b = int_number('Введіть ціле число b: ')

print(main())
