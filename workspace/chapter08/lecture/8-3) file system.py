import os

# 현재 작업 디렉터리
os. getcwd()

# 디렉터리 변경
os.chdir('chapter8')
os.getcwd()

# 현재 작업 디렉터리 목록
os.listdir('.')

# 디렉터리 생성
os.mkdir('test')
os.listdir('.')

# 디렉터리 이동
os.chdir('test')
os.getcwd()

# 여러 디렉터리 생성
os.makedirs('test2/tset3')
os.listdir('.')

# 디렉터리 이동
os.chdir('test2')
os.listdir('.')

# 디렉터리 삭제
os.rmdir('test3')
os.listdir('.')

# 상위 디렉터리 이동
os.chdir('../..')
os.getcwd()

# 여러개의 디렉터리 삭제
os.removedirs('test/test2')

# ..은 상위 디렉터리(디렉터리명을 몰라도)
# 현재경로를 기반으로 절대경로를 반환한다 -> 꼭대기 디렉터리부터 현재 디렉터리까지 모든 경로 파악


#glob모듈함수
#이스케이프
glob.escape(pathname,*,recursive=False)

# * -> *.a -> 모은 a확장자
# ? -> 한문자를 의미
# >>> ->프로그램 X 프롬프트 O