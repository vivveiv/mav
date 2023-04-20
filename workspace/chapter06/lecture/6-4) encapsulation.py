class account:
    __balance = 0
    __accname = 0
    __accno = 0

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accname = name
        self.__accno = no

    def getbalance(self):
        return self.__balance,self.__accname, self.__accno

    def setdeposit(self, money):
        if money < 0:
            print("금액 확인")
            return
        self.__balance += money

    def setwithdraw(self, money):
        if self.__balance < money:
            print("잔액 부족")
            return
        self.__balance -= money  #__balance든 balance든 상관없으나 __balance가 보기 좋다.

# 클래스에 대한 object 생성
acc = account(1000, "홍길동", "125-152-4125-41")

bal = acc.getbalance() # !!!!!!
print("계좌정보: ", bal)

acc.setdeposit(10000)
bal = acc.getbalance()
print("계좌정보: ", bal)
