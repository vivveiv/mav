#
def calc_func (a,b):
    x = a
    y = b
    def plus():
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

p, m = calc_func(10, 20)
print('plus=', p())
print('minus=', m())

class calc_class:
    x = y = 0

    def __init__(self, a, b):
     self.x = a
     self.y =b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class (10,20)

print('plus = ', obj.plus())
print('minus =', obj.minus())


#
class car:
    cc = 0
    door = 0
    cartype = ' '

    def __init__(self, cc, door , cartype):
        self.cc = cc
        self.door = door
        self.cartype = cartype

    def display(self):
        print ("자동차는 %d cc이고, 문짝은 %d 개, 타입은 %s" %(self.cc, self.door, self.cartype))

# 참조변수.멤버(할당시킬 '생성자와 똑같은 멤버변수' or 메서드)
car1 = car(2000, 4, "승용차")
car2 = car(3000, 5, "suv")

car1.display()
car2.display()