# 카운터와 누적변수
cnt = tot = 0
while cnt < 5:
    cnt += 1
    tot += cnt
    print(cnt, tot)


# 무한 루프

numData = []

while True :
    num = int(input("숫자 입력 :"))
    if num % 10 == 0 :
        print("프로그램 종료", "실패 숫자 모음="+ str(numData))
        break
    else :
        print(num)
        numData.append(num)


# random 관련 함수

# (1)random module 추가

import random
help(random)

# (2)random 모듈의 함수 도움말
help(random.random)

# (3) 0~1 사이 난수 실수
r = random.random()
print("r=", r)

# (4) 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True:
    r = random.random()
    print(r)
    if r < 0.01:
        break
    else:
        cnt +=1
print("난수 개수 = ", cnt) # cnt는 그 시점에서의 번호표구나

# (5) random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices)

# (6) 이름 list에 전체 이름, 특정 이름 출력
import random
names = ['홍길동', '이순신', '유관순']
print(names)
print(names[1])

# (7) list에서 자료 유무 확인하기
if "유관순" in names:
    print("유관순 있음")
else:
    print("유관순 없음")

# (7) 난수 정수로 이름 선택하기

idx=random.randint(1,2)
print(names[idx])


# break, continue 예
# break든 continue든 당첨되면 출력이 안된다.
i =0
while i <10:
    i+=1
    if i == 3:
        continue
    if i == 6:
        break
    print (i, end=' ')
