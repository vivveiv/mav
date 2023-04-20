# (1) 얕은 복사 : 주소 복사 (내용과 주소 모두 동일)
name = ['홍길동', '이순신', '강감찬']
print('name address =', id(name))

name2 = name
print('name2 address=', id(name2))

print(name)
print(name2)

# 원본 수정 : 함께 참조하는 주소에 수정하므로 한 변수의 값만 수정해도 두 변수의 값이 동시에 수정됨
name2 [0] = "김길동"
print(name)
print(name2)

# (2) 깊은 복사 : 내용 복사 (내용 동일, 주소 다름)
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)
print("name address =", id(name))
print("name3 address =", id(name3))

# 원본 수정 : 각자 다른 주소를 참조하므로 해당 변수의 주소에 해당하는 값만 수정됨
name[1] = "이순신장군"
print(name)
print(name3)