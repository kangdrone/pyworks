# 가변 매개 변수 : 매개변수가 정해지지 않음
# 문자열이 추가되는 함수

def merge_text(*text):
    result = ""  # 빈 문자 선언(초기화)
    for t in text:
        result += t
    return  result  # for 밖에서 return 함

# 숫자를 더해서 평균을 계산하는 함수
def calc_avg(*x):
    total = 0
    for i in x:         # for i in (1, 2, 3, 4)  튜플
        total += i
    avg = total / len(x)   # 개수 세는 함수 - len(x)
    return avg

# 제곱수 계산하는 함수 정의
def square(x):
    return x * x
if __name__ == "__main__":
    # 문자열 더하기
    text1 = merge_text("코스모스")
    text2 = merge_text("코스모스 ", "국화 ")
    print(text1)
    print(text2)

# 평균 계산
n1 = calc_avg(1, 2)
n2 = calc_avg(1, 2, 3, 4)
print(n1)
print(n2)