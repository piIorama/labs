__author__ = 'Marauder'
#-*- coding:utf-8 -*-
import re
str='+7-913-432-12-32, +7 (383) 432 1232,  +74213214213'
def Findnumber(str):
    match=re.findall(r'\+7\W?\W?\d\d\d\W?\W?\d\d\d\W?\d\d\W?\d\d',str)
    print match
Findnumber(str)
def Sum(name1):
    f = open(name1)
    f1=f.readline()
    summ=0
    while f1:
        match=re.search(r'(\d*)\s(\d*\.?\d*)\sr.',f1)
        #print match,match.group(1),match.group(2)
        summ+=float(match.group(1))*float(match.group(2))
        f1=f.readline()
    return summ
print Sum('invoice.txt')

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
print extract_names('baby1990.html')