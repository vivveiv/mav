import random

guesses = 0
numMin = 1
numMax = 100
userInput = ""

randNum = random.randint(numMin,numMax)

print(numMin, "와(과)", numMax , "사이의 숫자 하나를 정했습니다")
pritn("이 숫자는 무엇일까요?")

while randNum != userInput :
 userInput = int(input( "예상숫자:")) # 사용자 답 입력밥기 !!!!!!!
 guesses = guesses + 1 # 시도 횟수 1회 늘리기

    if userInput < randNum :
        print("작습니다. 다시 입력하세요.")
    elif userInput > randNum :
        print("큽니다. 다시 입력하세요.")
    else :
        print("정답입니다! 시도 횟수:", guesses, "번")
    break
 print("즐거우셨나요 또만나요")



# list 원소 추가 밎 요소 검사하기

size = int(input("vector 수 : "))

lst = []
for i in range(size):
    lst.append(size)

print("vector 크기 : ", len(lst))
