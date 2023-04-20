# 04/10

# project(1)

print("안녕하세요! 다음 질문에 답하고 이야기를 완성하세요.")

A=input("동물을 입력하세요: ")
B=input("이름을 입력하세요: ")
C=input("형용사를 입력하세요+(00(이)고)")
D=input("색을 입력하세요+(00색)")
E=input("형용사를 입력하세요+(000니다)")
F=input("명사를 입력하세요: ")
G=input("명사를 입력하세요: ")
H=input("명사를 입력하세요: ")
I=input("형용사를 입력하세요: ")
J=input("명사를 입력하세요:")
print("다음은 "+B+"이야기입니다.")

print("저의 반려동물은 "+A+"이며, 이름은 "+B+"입니다")
print(C+"(이)고 "+D+"색 이며 "+E+"니다.")
print(B+"은(는) "+F+G+H+"을(를) 먹습니다.")
print("가장 좋아하는 장난감은 "+I+" "+J+"입니다.")


# 04/11

# project (2)
su=5
dan=800
print("su 주소: ", id(su))
print("dan 주소: ", id(dan))
print("금액=", su*dan)

# project (3)
color1=(input("컬러1 :"))
print(color1)
color2=(input("컬러2 :"))
print(color2)
color3=(input("컬러3 :"))
print(color3)
print("="*30)
print("약자:", color1[0]+color2[0]+color3[0])

#or
color1=(input("컬러1 :"))
color2=(input("컬러2 :"))
color3=(input("컬러3 :"))
abbr=(color1[0]+color2[0]+color3[0])
print("="*30)
print("약자:"+abbr)