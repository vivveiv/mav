
# builtins 함수
# range(), sum(), max(), min()
dataset = list(range(1,6))
print(dataset)
print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

# import 함수
# 방법1
import statistics
#방법2
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))


# 사용자 정의 함수

# (1) 인수가 없는 함수

def userFunc1():
    print("인수가 없는 함수")
    print("userFunc1")

userFunc1()

# (2) 인수가 있는 함수

def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print ( 'z=', z)

userFunc2(10, 20)

# (3) return 있는 함수
def userFunc3(x,y):
    print('userFunc3')
    tot=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return tot, sub, mul, div

#실인수 : 키보드 입력
x = int (input ('x 입력:'))
y = int (input ('y 입력:'))


t, s, m, d = userFunc3(x,y)  !!!!!!!!!!!!!!!!!!!!!!!
print('tot=', t)
print('mul=', m)
print('sub=', s)
print('div=', d)
