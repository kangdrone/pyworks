# 사각형, 삼각형의 면적을 계산하는 함수

# 사각형
def square(w, h):
    area = w * h
    return area

# 삼각형
def triangle(w, h):
    area = int(w * h / 2)  # int() - 정수로 바꿀때 사용
    return area

# 너비 - 5cm, 높이 - 4cm인 도형 계산
area_rec = square(5, 4)
print("사각형의 면적 : ",area_rec)

area_tri = triangle(5, 4)
print("삼각형의 면적 : ",area_tri)
