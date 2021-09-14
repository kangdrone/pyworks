# 딕셔너리 자료구조
# 키와 값으로 이루어짐

person = {}   # 빈 딕셔너리 선언
person['name'] = '강신범'
person['age'] = 24
person['phone'] = '010-8487-5073'
person['gender'] = '남자'
print(person)

del person['age']   # age 요소 삭제
print(person)

person['name'] = '오상식' # 수정
print(person)