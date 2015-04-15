__author__ = 'Marauder'
#-*- coding:utf-8 -*-
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def raise_pay(self, percent):
        self.pay = self.pay *(100 + percent)/100

    def __str__(self):
        return '%s: %s, %s' % (self.__class__.__name__, self.name, self.pay)

y=Person('Jared Leto','actor',130000)
z=Person('Shannon Leto','actor',120000)
t=Person('Tomo Mi','actor',110000)

print y,z,t
class Manager(Person):
    def __init__(self,name,pay=1000):
        Person.__init__(self, name,'manager',pay)
    def raise_pay(self, percent,bonuse=10):
        Person.raise_pay(self,percent+bonuse)
r=Manager('System')
r.raise_pay(20,10)
print r
class Department():

    def __init__(self,dep):
        self.name=dep
        self.members=[]
        self.jobs=[]
        self.pays=[]
    def add_member(self,name,job,pay):
        self.members.append(name)
        self.jobs.append(job)
        self.pays.append(pay)
    def raise_pay(self, percent):
        temp=[]
        while self.pays:
            h=self.pays.pop()
            h = h *(100 + percent)/100
            temp.append(h)
        #print temp
        temp.reverse()
        self.pays=temp
        #print self.pays
    def group(self):
        print self.members
    def showmethemoney(self):
        print self.name
        print self.pays

x=Department('State')
y=Department('Notstate')
x.add_member('name','job',1000)
x.add_member('name','job',2000)
x.add_member('n2','job',3000)
y.add_member('n1','job',1000)
x.group()
x.showmethemoney()
x.raise_pay(10)
x.showmethemoney()
y.showmethemoney()

