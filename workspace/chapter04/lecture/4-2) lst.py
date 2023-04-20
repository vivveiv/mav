# 리스트 객체의 특징과 형식
# 순서자료구조를 갖는 열거형 객체
# 변수 = [값1, 값2, 값3 ....값n]
# 리스트의 원소는 무조건 0부터의 숫자로 색인이 매겨진다
# 콤마가 파티션이다 -> 콤마당 색인이 매겨진다

# 단일 lsst

lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[i-1:]) # :n 색인n까지 / n: 색인n부터


# 단일 list 색인

x = list (range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2]) # 홀수 색인
print(x[1::2]) # 색인1부터 시작하는 짝수 색인


# 중첩 list 색인

a = ['a', 'b', 'c']
print(a)

b = [10, 20, a, 5, True, '문자열'] # 서로 다른 자료형 리스트
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])
print(type(b))

# list 원소의 생성(리스트 타입의 변수 설정), 추가(내장함수append), 삭제(내장함수remove), 수정(=변수 대입), 삽입(내장함수insert)

num = ['one', 'two','three','four']
print(num)
print(len(num))
print('\n')

num.append('five')
print(num)
print()

num.remove('five')
print(num)

num[3] = '4'
print(num)

num.insert(0, 'zero')
print(num)


# 리스트 결합 (리스트 변수끼리 결합하면 원소를 합한 새 리스트 변수 생성가능)

x = [1,2,3,4]
y = [1.5, 2.4]
z = x+y
print(z)

# 리스트 확장 내장함수 ->결합과 같고 추가와 다르다 즉, extend(확장= 다른 변수집합에 있던 원소를 들임)

x.extend(y)
print(x)


# 리스트 추가 내장함수 append(추가= 다른 변수집합을 넣음 =부분집합)
x.append(y)
print(x)

# 리스트 두 배 확장 !!!!!!!!!!
lst = [1,2,3,4]
result = lst*2
print(result)


# 리스트 정렬(sort)

print(result)
result.sort() #오름차순 정렬
print(result)
result.sort(reverse=True) #내림차순 정렬
print(result)

# 리스트 요소 검사(관계 연산)

import random
r = [] #리스트 타입의 변수 초기화 설정
for i in range(5) :
    r.append(random.randint(1,5))
print(r)
if 4 in r :
    print ('있음')
else :
    print ('없음')



# 리스트 내포

# 변수 = [실행문 for] 즉, 변수x = [실행문 for 변수y in 열거형객체]
x = [2,4,1,5,7]

lst = [i**2 for i in x]
print(lst)

# 변수 = [실행문 for if] 즉, 변수x = [실행문 for 변수y in 열거형객체 if 조건식]
num = list(range(1,11))
lst2 = [ i*2 for i in num if i % 2 ==0]
print(lst2)


