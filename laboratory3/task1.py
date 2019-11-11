"""
Доповнити символом '*' слова, що мають довжину менше заданої (максимальної) до максимальної.
"""
import re
re_integer = re.compile('^\d+$')
re_string = re.compile('[A-Za-zА-Яа-яіІїЇьЙйЩщ ]+\s*')

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator1(pattern,promt):
    text = input(promt)
    while not bool(pattern.findall(text)):
        text = input(promt)
    return text

def str_words(promt):
    words = str(validator1(re_string, promt))
    return words

def int_num(promt):
    num = int(validator(re_integer, promt))
    return num

def main():
    words2 = []
    if sep in words:
        for word in words.split(sep):
            if len(word)<num:
                words2.append(word+(symb)*(num - len(word)))
            else:
                words2.append(word)
        return (', '.join(list(words2)))
    else:
        print('Не знайдено заданого роздільника!')

symb = input('Яким символом доповнюємо слова? ')
sep = input('Роздільник між словами у вашому рядку: ')
words = str_words('Введіть рядок слів: ')
num = int_num('Введіть максимальну кількість символів у слові: ')

print('Отриманий рядок: ', main())