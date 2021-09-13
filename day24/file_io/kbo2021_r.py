# 리스트 읽기

try:
    f = open("c:/pyfile/kbo2022.txt", 'r')
    date = f.read()
    print(date)
    f.close()
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')