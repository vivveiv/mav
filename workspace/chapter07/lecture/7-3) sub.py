# 파이썬 매서드 replace는 정규식 패턴에 대응하는 문자열을 찾아주지는 못한다.
# 그래서 re.sub 메서드가 필요하다.
# 단어의 "조사"같은 걸 제거하고 나머지만 남기고 싶을 때 주로 사용함.

from re import sub
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text1 = sub('[\^*$]+', '', st3)
print(text1)


text2 = sub('[0-9|a-z]', '', text1)
print(text2)

