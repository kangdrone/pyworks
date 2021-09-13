# 파일 읽기 - read() 함수 사용

f = open("c:/pyfile/file.txt", 'r')
date = f.read()   # 파일 내용을 읽어서 date에 저장
print(date)

f.close()

f = open("c:/pyfile/number2.txt", 'r')
date = f.read()   # 파일 내용을 읽어서 date에 저장
print(date)

f.close()