class Employee :
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    def pay_calc(self, base, bonus):
        pass

class Permanent (Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus ):
        self.pay = base + bonus
        print("총 수령액: ", format(self.pay, "원"))

class Temporary (Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print("총 수령액 : ", format(self.pay, "원"))


    empType = input ("고용형태 선택 (정규직<P>, 임시직<T>) : " )
    if empType == "P" or empType == "p" :
        pname = input("이름: ")
        base = int(input("기본급: "))
        bonus = int(input("상여금: "))
        presultpay = base + bonus
        print ("고용형태 : 정규직 ", "이름:", pname, "급여: ", presultpay )


    elif empType == "T" or empType == "t" :
        tname = input("이름: ")
        tpay = int(input("시급: "))
        time = int(input ("작업시간: "))
        tresultpay = tpay * time
        print ("고용형태 : 임시직", "이름:", tname, "급여: ", tresultpay)

    else :
        print ('='*30)
        print ('입력 오류')