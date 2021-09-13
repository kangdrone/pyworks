"""
- 영어 타자 연습 게임
* 게임이 시작되면 영어 단어가 화면에 표시됨
* 사용자는 최대한 빠르고 정확하게 입력해야 함
* 바르게 입력했으면 "통과"를 출력하고 다음 문제가 출제됨
* 오타가 있으면 "오타! 다시 도전"이 출력되고 같은 단어가 한 번 더 나옴
* 타자 게임 시간을 측정함

"""
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry',
        'graoe', 'garlic', 'onion', 'potato']

n = 1   # 문제 번호

print("[ 타자 게임 ] 준비되면 엔터")
input()
start = time.time()
while n < 11:
        print('-문제', n)
        q = random.choice(word)   # 문제
        print(q)
        u = input()   # 사용자가 입력
        # 논리 연산 코드 작성
        if u == q:
            print("통과")
            n += 1
        else:
            print("오타! 다시도전")
end = time.time()
et = end - start
print("타자 시간 : %.2f초" % et)