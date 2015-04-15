#!/usr/bin/python
# -*- coding:utf-8 -*-
# Списки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более, 
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.
def match_ends(words):
    i=0
    j=0
    while i<len(words):
        g=words[i]
        z=g[:1]
        l=len(g)
        y=g[l-1:]
        #print z
        #print y
        if z==y and l>=2:
            j+=1
        i+=1
    #print words
    return j


# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков
def front_x(words):
    i=0
    j=0
    l=[]
    j=[]
    k=words
    while i<len(k):
        g=k[i]
        z=g[:1]

        if z=='x':
            h=k[i]

            l.append(h)
        else:
            h=k[i]
            j.append(h)
        i+=1
    j.sort()
    l.sort()
    z=l+j
    return z


# C. Сортировка по последнему числу
# Дан спискок непустых списков. 
# Нужно вернуть список, отсортированный по 
# возрастанию последнего элемента каждого подсписка.
# Например: из [[1, 7], [1, 3], [3, 4, 5], [2, 2]] получится
# [[2, 2], [1, 3], [3, 4, 5], [1, 7]]
# Подсказка: используйте параметр key= функции сортировки, 
# чтобы получить последний элемент подсписка.

def sort_last(lists):

    def sortlast(s):
        return s[-1]
    lists.sort (key=sortlast)
    return lists



# D. Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4].
def remove_adjacent(nums):
    l=[]
    for i in nums:
        l.append(i)
        break
    i=0
    while i<len(nums):
        if nums[i-1]==nums[i]:

            pass
        else:
            l.append(nums[i])
            if l[0]==l[1]:
                l.remove(l[0])
        i+=1
    return l


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))



# Вызывает фунции выше с тестовыми параметрами.
def main():

    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
           [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
    test(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
    test(remove_adjacent([]), [])


if __name__ == '__main__':
  main()
