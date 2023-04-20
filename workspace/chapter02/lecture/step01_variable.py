# 1. 변수, 자료형객체, 메모리 주소

var1 = "Hello python"
print (var1)
print (id(var1))

var1 = 100
print (var1)
print (id(var1))
print (type(var1))

var2 = 150.25
print (var2)
print (id(var2))
print(type(var2))

var3 = True
print (var3)
print (type(var3))
print (id(var3))

print (var1)
print (id(var1))


# 2. 예약어 확인

import keyword # 모듈 임포트
python_keyword = keyword.kwlist #????
var4= python_keyword
print("파이썬 타입 리스트", var4)

print(type(python_keyword))
print(len(python_keyword)) # len=length=길이


# 3. 자료형 변환 "casting type"

# 실수->정수

a = int(10.5)
b = int(20.42)
add = a+b
print ('add = ', add)

# 정수->실수
a = float (60)
b = float (20)
print ('add2 = ', a+b)

print(a+b)

# 논리형 -> 정수
print(int (True)) #1
print(int (False)) #0

# 문자형 -> 숫자형
st = "11.7"
print(float(st) **2) #제곱연산

# 그냥 내가 응용해봄
import keyword
apfhd_keyword = keyword.softkwlist
print(apfhd_keyword)


# 4. 연산자 익히기

# 4-1. 산술연산
num1= 100 #피연산자1
num2= 20 #피연산자2

print("<산술연산결과목록>")
add = num1 + num2
print ("add =", add)
sub = num1 - num2
print ("sub =", sub)
mul = num1 * num2
print ("mul =", mul)
div = num1 / num2
print ("div =", div)
div2 = num1 % num2
print ("div2 =", div2)
square = num1 **2
print ("square =", square)

# 4-2. 관계연산

num1= 100 #피연산자1
num2= 20 #피연산자2

print("<관계연산결과목록>")
print("(1)동등비교")
bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)
print("(2)크기비교")
bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

# 4-3. 논리연산

num1= 100 #피연산자1
num2= 20 #피연산자2

print("<논리연산결과목록>")
log_result = num1 >=50 and num2 <=10
print(" num1 >=50 and num2 <=10의 논리값은? ", log_result, "이다.")
log_result = num1 >=50 or num2 <=10
print(" num1 >=50 or num2 <=10의 논리값은? ", log_result, "이다.")
log_result = num1 >=50
print(" num1 >=50의 논리값은? " , log_result, "이다.")
log_result = not(num1 >=50)
print(" not (num1 >=50)의 논리값은? ", log_result, "이다.")

# 4-4. 대입연산

#복합연산

i=tot=10 # i=10; tot=10
print("i=10이고 tot=10일 때")

i+=1 # i=i+1
tot+=i # tot=tot+i
print("i+=1는", i, end=' 이고 ')
print("tot+=i는", tot, '이다.')

#같은 줄에 중복 출력

print ('출력1', end=' , ')
print ('출력2')

#교체 swapping

v1, v2 =100, 200
v2,v1=v1,v2
print(v1, v2)

#패킹 packing 할당

lst = [1,2,3,4,5]
v1, *v2, v3= lst
print(v3)

*v1, v2, v3 =lst
print(v1, v2, v3)