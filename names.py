# -*- coding: utf-8 -*- 
#!/usr/bin/python

import sys
import os
import re

"""Упражнение "Имена"

Есть статистика популярности имен которыми называют детей в США по годам.
Данные представленны в HTML файле. 

Так выглядит HTML c именами который предстоит разобрать:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

1. Создайте функцию extract_names(filename), которая принимает в качестве 
аргумента имя файла и возвращает данные из него в виде списка вида:
babynames =  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]


2. В функции main() выведите список на экран построчно т.е.:

"
2006
Aaliyah 91
Aaron 57
Abagail 895
"
и т.д.

Если указан аргумент --summaryfile то вместо вывода на экран сохраните этот вывод в файл 
с расширением .summaryfile например:
"2006.summaryfile"

разбейте решение на части:
- извлеките и напечатайте год
- извлеките и напечатайте имена и порядковые номера 
- поместите данные об именах в словарь и выведите словарь на экран
- сформируйте список вида [year, 'место в списке', ... ] и выведите его на экран 
- попправьте main() для использования списка extract_names

"""
def extract_names(filename):
    babynames=[]
    f = open(filename,'r')
    f1=f.readline()
    while f1:
        #print(f1)
        try:
            match1=re.search(r'Popularity in\s(\d*)',f1)
            babynames.append(match1.group(1))
        except AttributeError:
            pass
        match=re.search(r'\S*\salign="right"><td>(\d*)<\/td><td>(\w*)<\/td><td>(\w*)<\/td>',f1)
        try:
            #print match,match.group(1),match.group(2)
            x=match.group(2)+' '+match.group(1)
            babynames.append(x)
            x=match.group(3)+' '+match.group(1)
            babynames.append(x)

        except AttributeError:
            pass
        f1=f.readline()
    babynames.sort()
    return babynames
#print extract_names('baby1990.html')

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]



if __name__ == '__main__':
    main()
