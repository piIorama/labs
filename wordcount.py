#!/usr/bin/python
#-*- coding:utf-8 -*-
"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее
часто встречающихся слов, таким образом первым будет самое часто встречающееся
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys
def visual(d):
    for i in sorted(d):
        y=d.get(i)
        print 'Слово',i,'Количество',y
def open_input(filename):
    f=open(filename,'r')
    l=[]
    z=f.read()
    z=z.lower()
    z=z.strip()
    z=z.replace(',','')
    z=z.replace('.','')
    z=z.replace(':','')
    z=z.replace(';','')
    z=z.replace('"','')
    z=z.replace('!','')
    z=z.replace('+','')
    z=z.lower()
    z=z.split()
    return z
def print_words(filename):
    d = {}
    z=open_input(filename)
    for i in z:
        y=0
        x=int(d.setdefault(i,y))
        y={i:x+1}
        d.update(y)
    visual(d)
def print_top(filename):
    d = {}
    z=open_input(filename)
    for i in z:
        y=0
        x=int(d.setdefault(i,y))
        y={i:x+1}
        d.update(y)
    x=d.values()
    y=d.keys()
    l=zip(x,y)
    j=-1
    for i in reversed(sorted(l)):
        j+=1
        if j<=20:
            print 'Слово',i[1],'встречается',i[0],'раз'
    return
# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Напишите также  вспомогательную функцию word2dict, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.
#print_words('test.txt')
#print 'I am '
#print_top('test.txt')
###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
    main()

