# with ~ as 구문 : close()를 사용 안함
# 원의 넓이 계산 = PI * 반지름 * 반지름
import math

with open("c:/pyfile/circle_area.txt", 'w') as f:
    radius = 10
    area = math.pi * radius * radius
    f.write("반지름의 길이 : %dcm\n" % radius)
    f.write("원의 넓이 : %.2fcm\n" % area)