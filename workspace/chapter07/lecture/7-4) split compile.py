from re import split, match, compile

multi_line= """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

web_site= split('\n', multi_line)
print(web_site)                   # 함수를 먹인 변수를 출력해보자

pat = compile('http://')   # 객체 함수 먹여서 변수 만들기

sel_site = [site for site in web_site if match(pat, site)]
print(sel_site)