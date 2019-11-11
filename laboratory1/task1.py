"""
Дано значення температури в градусах Цельсія. Вивести температуру в градусах Фаренгейта.
"""
import re
re_float = re.compile('^[+-]{0,1}\d+(\.){0,1}\d*$')

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def what_temp():
    run = input('Оберіть дію (1-перетворення з C у F, 2-перетворення з F у C): ')
    if run == '1':
        return celsius()
    elif run == '2':
        return fahrenheit()
    else:
        return what_temp()

def celsius():
    temp = float(validator(re_float, 'Введіть температуру в градусах Цельсія: '))
    return temp+273.15

def fahrenheit():
    temp = float(validator(re_float,'Введіть температуру в Фаренгейтах: '))
    return temp-273.5

print(what_temp())