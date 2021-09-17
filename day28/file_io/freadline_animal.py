
with open('animal.txt', 'w') as f:
    animal = ['dog', 'cat', 'horse', 'cow']
    for i in animal:
        f.write(i + '\n')

with open('animal.txt', 'r') as f:
    # line = f.readline()   # 한줄 읽기
    # print(line)

    lines = f.readlines()   # 전체 읽기
    print(lines)   # 1차원 리스트

    # 2차원 리스트 만들기
    animal = []
    for i in lines:
        # animal.append([i])
        animal.append(i[0:-1])    # 1차원
        # animal.append([i[0:-1]])  # 2차원
    print(animal)

    # for i in lines:
    #     print(i, end='')