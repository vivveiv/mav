# 튜플
# 변수 = (값1, 값2, .... 값n)
# 읽기 전용이기 때문에 값을 추가(append함수), 삽입(insert함수), 수정, 삭제(remove함수) 할 수 없다.

# (1)원소가 한 개인 경우
t=(10, )
print(t)

# (2)원소가 여러 개인 경우
t2 = (1,2,3,4,5,3)
print(t2)

# (3) 튜플 색인
print(t2[0], t2[1:4], t2[-1])

# (4) 수정 불가
t2[0] =10

# (5) 요소 반복
for i in t2 :
    print(i, end=' ')

# (6) 요소 검사
if 6 in t2 :
    print("6있음")
else :
    print("6없음")


# 튜플 관련 함수

lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3.count(3))
print(t3) #!!!!!!



