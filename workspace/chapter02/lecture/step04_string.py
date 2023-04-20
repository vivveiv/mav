# 1.유형별 문자열 변수 설정

oneLine = "thins is one line string"
print(oneLine)

multiLine = """this is
three line
string"""
print(multiLine)

multiLine2 = "this is \nthree line\nstring"
print(multiLine2)


# 2.문자열의 색인

string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# 3.문자열의 연산
print("python" + "program")
# print ("python-" + 3.7 + ".exe")
print("python-" + str(3.7) + ".exe")  # 숫자 3.7을 문자타입으로 출력
print("python-" + "3.7" + ".exe")  # 문자 3.7을 출력
print("-"*30)  # 반복 연산


# 4.슬라이싱

oneLine = "thins is one line string"

print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0 : 4])
print(oneLine [:4])
print(oneLine[:])
print(oneLine[::2])

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

substring = oneLine[-11]
print(substring)


# 5.문자열 처리 함수

tom = "this is one line string"

# 5-1. 특정 글자 수 반환
print("t 글자수:", tom.count("t"))

# 5-2. 접두어 문자 비교 판단
print(tom.startswith("this"))
print(tom.startswith("that"))

# 5-3. 문자열 교체
print(tom.replace("this", "that"))

# 5-4. 문자열 분리(split) : 문단 -> 줄별
tommy = """this is
three line
string"""
line = tommy.split("\n")  # \n단위로 나눠라
print("라인:", line)

# 5-5. 문자열 분리(split2) : 문장 -> 단어

words = tommy.split(" ")
print("단어:", words)

# 5-6. 문자열 결합(join) : 단어 -> 문장
sent = " ".join(words)
print(sent)
