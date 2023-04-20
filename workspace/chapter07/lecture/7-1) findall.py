from re import findall

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

print(findall('1234',st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))

print(findall('[가-힣]{3,}',st1))
print(findall('[a-z]{3}', st1))
print(findall('[a-z|A-Z]{3}', st1))

st2 = 'test1abcABC 123mbc 45test'

print(findall('^test', st2)) # '단어'의 접두어
print(findall('st$', st2)) # '단어'의 접미어
                           # 45test의 접미어 출력임
                           # test1abcABC의 중간 문자열을 출력한게 아님

st2 = 'test1abcABC 123mbc 45test'
print(findall('.bc', st2))

##### 단어단위 상관없이 특정 문자열로 끝나는 범위 출력?

print(findall('t.', st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)
print(words)

print(findall('[^^*$]+', st3))