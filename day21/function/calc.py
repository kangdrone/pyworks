"""
함수 정의
 . 조건 - 두 수를 매개변수로 전달하여 서로 같으면 곱하고
         서로 다르면 더하는 함수
"""
def date(x, y):
    if x == y:
        return x * y
    else:  # x ! = y
        return x + y



n1 = date(5, 5)  # 25
n2 = date(5, 6)  # 11

print("n1 = %d" % n1)
print("n2 = %d" % n2)