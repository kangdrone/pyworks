# 3번 예제 <점프 투 파이썬 p.112>
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4번 예제 <점프 투 파이썬 p.113> 성별 문자가 1이면 '남자', 아니면 '여자'
print(pin[7])
if pin[7] == '1' or pin[7] == '3':
    print("남자")
else:
    print("여자")

# 5번 예제 <점프 투 파이썬 p.113>
a = "a:b:c:d"
b = a.replace(':', '#')  # 이전문자, 새로운문자
print(b)

# 6번 예제 <점프 투 파이썬 p.113> 
a = [1, 3, 5, 4, 2]
a. sort()
print(a)
a. reverse()
print(a)

# 7번 예제 <점프 투 파이썬 p.113> 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
