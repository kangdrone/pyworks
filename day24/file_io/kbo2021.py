# 리스트 자료를 파일에 쓰고 읽기

f = open("c:/pyfile/kbo2021.txt", 'w')
team = ['NC', '키움', '기아', '삼성', '롯데', 'SSG', 'LG', 'KT']

for i in team:   # 리스트형은 반복해서 쓰기
    f.write(i + '  ')

f.close()