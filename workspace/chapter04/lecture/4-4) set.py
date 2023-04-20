
# 셋set
# 여러 개의 자료를 "비순서"로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스이다.
# 콤마가 있어도! 콤마가 파티션을 뜻하지 않는다.
# 형식 -> 변수 = { 값1, 값2, 값3... 값n}

# (1) 중복을 취급하지 않는다.
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)

# (2) 요소 반복
for d in s :
    print (d, end=' ')
print()

# (3) 집합관련 함수
s2 = {3, 6}
print(s.union(s2)) # 합집합
print(s.difference(s2)) # 차집합
print(s.intersection(s2)) # 교집합

# (4) 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7) # 변수x.add(원소y) 원소 추가
print(s3)

s3.discard(3) # 변수x.discard(원소y) 원소 삭제
print(s3)


# set을 거쳐서 list 중복 원소 없애기

gender = ['남', '여', '남', '여']
print(gender)
print()
sgender = set(gender)
lgender = list(sgender)
print(lgender)
print()
print(lgender[1])