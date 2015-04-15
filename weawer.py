#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'Marauder'
# Строки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Пончики
# Дано количество пончиков (целое число);
# Нужно вернуть строку следующего вида:
# 'Количество пончиков: <count>', где <count> это количество,
# переданное в функцию как параметр.
# Однако, если количество 10 и более - нужно использовать слово
# 'много', вместо текущего количества.
# Таким образом, donuts(5) вернет 'Количество пончиков: 5'
# а donuts(23) - 'Количество пончиков: много'

def donuts(count):
    if int(count)>=10:
        count=str('Number of donuts: many')
    else:
        count=str('Number of donuts: ')+str(count)
    # +++my code is here+++
    return count


# B. Оба конца
# Дана строка s.
# Верните строку, состоящую из первых 2
# и последних 2 символов исходной строки.
# Таким образом, из строки 'spring' получится 'spng'.
# Однако, если длина строки меньше, чем 2 -
# верните просто пустую строчку.
def both_ends(s):
    x=len(s)
    if x<=2:
        s=str('')
    else:
        s=s[:2]+s[-2:]
    # +++my code is here+++
    return s


# C. Кроме первого
# Дана строка s.
# Верните строку, в которой все вхождения ее первого символа
# заменены на '*', за исключением самого этого первого символа.
# Т.е., из 'babble' получится 'ba**le'.
# Предполагается, что длина строки 1 и более.
# Подсказка: s.replace(stra, strb) вернет версию строки,
# в которой все вхождения stra будут заменены на strb.
def fix_start(s):
    x=s[:1]
    s=s.replace(x,'*')
    s=x+s[1:]
    # +++my code is here+++
    return s


# D. Перемешивание
# Даны строки a и b.
# Верните одну строку, в которой a и b отделены пробелом '<a> <b>',
# и поменяйте местами первые 2 символа каждой строки.
# Т.е.:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Предполагается, что строки a и b имеют длину 2 и более символов.
def mix_up(a, b):
    x1=a[:2]
    x2=b[:2]
    a=a[2:]
    b=b[2:]
    a=x2+a+' '
    b=x1+b
    s=a+b
  # +++my code is here+++
    return s

# E. Хорош
# Дана строка.
# Найдите первое вхождение подстрок 'не' и 'плох'.
# Если 'плох' идет после 'не' - замените всю подстроку
# 'не'...'плох' на 'хорош'.
# Верните получившуюся строку
# Т.о., 'Этот ужин не так уж плох!' вернет:
# Этот ужин хорош!
def not_bad(s):
    x=s.find('не')
    y=s.find('плох')
    if x<y:
        s=s[:x]+s[y:]
        s=s.replace('плох','хорош')
  # +++my code is here+++
    return s

# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s Получено: %s | Ожидалось: %s' % (prefix, got, expected)


# Вызывает фунции выше с тестовыми параметрами.
def main():

    print 'donuts'
    #Каждая строка вызывает donuts() и сравнивает возвращаемое значение с ожидаемым.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')


    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print()
    print 'Хорош'
    test(not_bad('Этот фильм не так уж плох'), 'Этот фильм хорош')
    test(not_bad('А ужин был не плох!'), 'А ужин был хорош!')
    test(not_bad('Этот чай уже не горячий'), 'Этот чай уже не горячий')
    test(not_bad("Этот плох, но не совсем"), "Этот плох, но не совсем")
    print "ВИВЕРОЧЕК ВИВЕРОК %)"

# Стандартный шаблон для вызова функции main().
if __name__ == '__main__':
  main()

