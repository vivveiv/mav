
# 최댓값 / 최솟값 알고리즘

import random
dataset = []
for i in range(10):
    r=random.randint(1, 100)
    dataset.append(r)
print(dataset)

# (2) 변수 초기화

vmax = vmin = 0

# (3) 최댓값/ 최솟값 구하기
for i in dataset :
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

# (4) 결과 출력
print ('max=', vmax, 'min=', vmin)


# 오름차순 정렬 (ascending sort)  # i는 기준 원소 j는 비교 원소
dataset = [3, 5, 1, 2, 4]
n = len (dataset)
for i in range (0, n-1) :
    for j in range (i+1, n) :
        if dataset [i] > dataset [j] :
            tmp = dataset [i]
            dataset [i] = dataset [j]
            dataset [j] =tmp
    print(dataset)      #각 회전 정렬내용

print(dataset)

# 내림차순 정렬 (descending sort)  # i는 기준 원소 j는 비교 원소

dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] < dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] =tmp
    print(dataset)

print(dataset)



num = int(input('점수 입력(1~100) :'))
print('num =', num)

if num % 2 != 0 :
    print('홀수')
else :
    print('짝수')

# 이진 검색 알고리즘

dataset = [5, 10, 18, 22, 35, 55 ,75,103]
value = int(input("검색할 값 입력 : "))

low = 0  # start 위치
high = len(dataset) - 1  # end 위치
loc = 0
state = False  # 상태 변수

while (low <= high) :
    mid = (low + high) // 2

    if dataset [mid] > value :  # 중앙값이 큰 경우
        high = mid - 1
    elif dataset [mid] < value :  # 중앙값이 작은 경우
        low = mid + 1
    else :  # 찾은 경우
        loc = mid
        state =True
        break
  if state :
    print('찾은위치 : %d 번째' % (loc +1))
  else :
    print("찾는 값은 없습니다")