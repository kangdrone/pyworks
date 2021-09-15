# readlines()는 자료를 리스트로 반환
# 리스트형 자료를 랜덤하게 추출하기
import random

try:
    with open("C:/pyfile/kbo2021.txt", 'r') as f:
        """
        lines = f.readline()
        print(lines)          # 리스트로 반환
        for line in lines:    # 요소 값 출력
            print(line)
        """
            # 요소를 구분기호로 구분 = split()함수
        data = f.readline().split()   # 공백문자로 구분
        print(data)
        team = random.choice(data)
        print(team)
except:
    print("파일을 찾을 수 없습니다")