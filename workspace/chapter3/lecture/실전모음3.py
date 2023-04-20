cnt = tot =0
pink = [] # 리스트는 []로 표현한다

while cnt <100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        pink.append(cnt)
print("1 ~ 100 사이 3의 배수 합 = %d" % tot)
print("dataset =", pink)

# 중첩 반복문
# range() 함수를 이용한 구구단 출력

for i in range(2, 10):
    print("~~~ {}단 ~~~".format(i))

    for j in range(1, 10):
        print("%d*%d=%d" % (i, j, i * j))


while True :
    kg = int(input('짐의 무게는 얼마입니까?'))
    if kg == 0 :
        break;
    if kg >=10 :
        price = (kg // 10 ) *10000
        print('수수료는' + format(price, '3,d') +'입니다')
    else :
        print('수수료는 없습니다')


while True:
    kg = int(input('짐의 무게는 얼마입니까?'))
    if kg == 0:
        break;
    if kg >=10:
        price = (kg // 10) *10000
        print('수수료는' + format(price, '3,d') + '입니다')
    else:
        print('수수료는 없습니다')