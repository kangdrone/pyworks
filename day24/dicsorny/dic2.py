# 딕셔너리의 주요 메서드
# pop() - 삭제, key() - 키, valuse() - 값

dic = {'Tomas':13, 'Jane':9}

# 요소 추가
dic['Mike'] = 10
dic['Elsa'] = 17
print(dic)

# 요소 삭제
dic.pop('Tomas')
print(dic)

# 모든 키 가져오기
print(dic.keys())   # 리스트 형태로 가져옴
for key in dic:   # 값 형태로 가져옴
    print(key)

# 모든 vaule 가져옴
print(dic.values())
for key in dic:
    print(dic[key])   # key로 접근해서 값을 가져옴