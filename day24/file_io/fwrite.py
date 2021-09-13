# 파일입출력
# 파일 열기 - 파일 쓰기 - 파일 종료

f = open("c:/pyfile/file.txt", 'w')
f.write("하늘\n")
f.write("Good Luck\n")
f.write('300\n')   # 숫자는 저장이 안됨

f.close()