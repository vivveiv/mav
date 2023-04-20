
# 중첩함수
# 외부함수는 내부함수를 return 해준다

# 일급 함수
def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b
b = a()  # 외부 함수 호출 : a 함수 -> def a
b()  # 내부 함수 호출 : b 함수 -> def b

# 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataset = data  # 이해를 돕기위한 변수 설정
    def tot():
        tot_val= sum(dataset)
        return tot_val
    def avg(tot_val):
        avg_val= tot_val / len(dataset)
        return avg_val  # inner 반환
    return tot, avg

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부 함수 호출 :
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)

# 정말인지 확인해보기
q=5050
print(avg(q))


# 산포도를 구하는 중첩함수



from statistics import mean
from math import sqrt
data= [4, 5, 3.5, 2.5, 6.3, 5.5]
def scattering_func (data):
    dataSet = data
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    def var_func(avg):
        diff = [ (data - avg) ** 2 for data in dataSet]
        var_val = sum(diff) / (len(dataSet) -1)
        return var_val
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func
avg,var,std = scattering_func(data)


print('평균:', avg())
print('분산:', var(avg()))
print('표준편차:', std(var(avg())))


# 획득자와 지정자

# (1) 중첩함수 정의
def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value + 30
    return getter, setter

getter, setter = main_func(100)

print('num =', getter())

setter(200)
print('num= ', getter())


# 함수 장식하기

 #(1) 래퍼 함수
def wrap (func) :
    def decorated() :
        print('반가워')
        func()
        print('잘가')
    return decorated()

@wrap
def hello() :
    print('어쩌구', '저쩌구')

hello()


#  재귀 함수
  # 반복적으로 호출하기 때문에 반드시 탈출(exit)조건이 필수이다.
  # 알고리즘에서 이용된다.
  # ex) 수열의 합, 팩토리얼 계산 등

def Counter(n):
    if n ==0:
        return 0  #종료 조건 # True가 되면서 결과값이 호출된다
    
    else:
        Counter(n-1)
    print(n, end=" ") #재귀호출

print('n=0 : ', Counter(0))  #Counter 함수가 아니다 내부 함수가 아니다

Counter(5)


# 누적합
# 1~n 정수 누적합
 # (1) 재귀함수 정의 : 1~n 누적합 (1+2+3+4+5=15)

def Adder(n):
    if n == 1:
        return 1
    else:
        result = n + Adder(n-1)

        print (n, end = ' ') # 스택 영역
        return result

print('n=1 :', Adder(1))

print('\nn=5 :', Adder(5))


