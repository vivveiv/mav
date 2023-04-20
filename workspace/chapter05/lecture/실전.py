# 문제 1

def starcount(height):
    h_cnt = s_cnt = 0

    while h_cnt < height:
        h_cnt += 1
        print('*' * h_cnt)
        s_cnt += h_cnt

    return s_cnt

print('star 개수 : ', starcount(3))


# 문제 2

def bank_account(bal):
    balance = bal

    def getbalance():
        return balance

    def deposit(money):
        nonlocal balance
        getbalance += money

    def withdraw(money):
        nonlocal balance
        balance -= money

    return getbalance, deposit, withdraw


bal=int(input("최초 계좌의 잔액을 입력하세요: "))
getbalance, deposit, withdraw = bank_account(bal)

print("현재 계좌 잔액은 "+ str(getbalance())+ "입니다.")

money= int(input("입금액을 입력하세요")