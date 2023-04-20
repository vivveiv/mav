# for 반복문 (반복 출력)

 # (1) 문자열 열거형객체 이용
string = "홍길동"
print(len(string))
for s in string:
    print(s)

 # (2) list 열거형객체 이용
lstset = [1, 2, 3, 4, 5]
for e in lstset :
    print("원소: ", e)


#range 클래스(=범위)명령문

 # (1) range 객체변수 생성
num1 = range(10)
print("num1: ", num1)

num2 = range(1,10)
print("num2: ", num2)

#range(1,10)은 range(0,10)과 비교했을 때, 정수 "0"인 왼쪽 한칸이 없다
num3 = range(1,10,2)
print("num3: ", num3)

# (2) range 객체변수 활용
for n in num1 :
    print(n, end=" ")
print( )
for n in num2 :
    print(n, end=" ")
print( )
for n in num3 :
    print(n, end=" ")


# array (for&lisst)

 # (1) list에 자료 저장하기
lst = []
for i in range(10) :
    r = random.randint (1,10) # 난수 발생
    lst.append(r) # 난수 저장

print("lst=", lst) # 난수 출력

# (2) list에 자료 참조하기
for i in range(10) :
    print(lst[i] * 0.25)


# 중첩 반복문 (for, while)

for 변수1 in range()
    print(변수1)
    for 변수2 in range()
        print(변수2)

while
    print()
    while
        print()
while
    while
    print()
print()
