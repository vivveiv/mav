class multiply :
    x = y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = multiply(10, 20)
print('곱셈=', obj.mul())

class sum:
    x = y = 0

    # 객체
    def __init__(self):
        pass
    def data(self, x, y):
        self.x = x
        self.y = y

    # 행위
    def sum(self):
        return self.x + self.y

obj = sum()
obj.data(10,20)
print('덧셈=', obj.sum())


#멤버변수와 생성자가 없는 경우
class multiplay3:

    def data (self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        result = self.x * self.y
        self.display(result)
    def display(self, result):
        print("곱셈 = %d" % (result))

obj = multiplay3() #기본 생성자
obj.data(10,20) #멤버 참조
obj.mul()


