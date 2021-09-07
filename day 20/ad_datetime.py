# dateitme 모듈 - 날짜, 시간 관련
import datetime

now = datetime.datetime.now()
print(now)

# 날짜
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))

# 시간
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

print("{}년 {}월 {}일, {}시 {}분 {}초".format(now.year,
                now.month, now.day, now.hour, now.hour, now.minute, now.second))

# 날짜/시간 출력
print(now.strftime("%Y. %m. %d %H. %M. %S"))

print("지금까지 몇 일?")
day1 = datetime.datetime(2021, 8, 10)  # 날짜 설정
print(day1)
today = datetime.datetime.today()  # 오늘 날씨
print(today)

passed_time = today - day1  # 오늘 - 특정한 날
print("개강이후 {}일이 지났습니다.".format(passed_time.days))
