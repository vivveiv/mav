
# 딕트(dict)
# 여러개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조인 열거형 객체를 생성하는 클래스
# 콤마가 있어도! 콤마가 파티션을 뜻하지 않는다.
# 형식-> 변수 = dict {'키' : '값' , '키' : '값' ....'키':'값'} 등
# 색인 대신에 키로 값을 찾는다. ->원소의 수정, 삭제, 추가등이 가능하다.
# -> 원소의 수정, 삭제, 추가등이 가능한지의 여부는 변수가 순차or비순차 자료구조인지 여부에 달린 것이 아니라 키나 인덱스처럼 불러낼 변수가 있는지의 여부이다.

# (1) 생성방법 -> dict()
dic = dict(key1 = 100 , key2 = 200, key3 = 300)
print(dic)

# (2) 생성방법 -> {}
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가 -> []  #대입연산자"[]"
person = {'name':'홍길동', 'age':35, 'address':'서울시'}

person['age']=45
print (person)

del person['address'] # key를 삭제하면 해당 value도 뜨지 않는다.
print (person)

person['pay']=350
print(person)

person.append('pay': 350) #!!!!!!!


# 요소 검사

print (person['age']) #-> 변수객체 dict의 키의 값 검사
print ('address'in person) #-> 변수 객체 dict의 키의 존재여부 검사

# 요소 반복

for key in person.keys():  # 변수객체.keys()  !!! 괄호안을 비운다
    print(key)
for v in person.values():   # 변수객체.values()
    print(v)
for i in person.items() :   # 변수객체.items()
    print(i)


# 단어의 빈도수 구하기
charset = ['abc', 'code', 'band', 'band', 'abc']
wc={}

for key in charset :
    wc[key] = wc.get(key, 0 )+1

print(wc)