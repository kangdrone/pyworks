# 구구단 출력
"""
x = input("단을 입력하세요 : ")
dan = int(x)

for i in range(1, 10):
    print(dan, "x", i, "=", dan*i)
"""

# 전체 구구단 출력
for i in range(2, 10):
    print("[", i, "단 ]")
    for j in range(1, 10):
        #print(i, "x", j, "=", i*j)
        print("%d x %d = %d" % (i, j, i*j))
    print()
