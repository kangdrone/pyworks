with open('word.txt', 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry',
        'graoe', 'garlic', 'onion', 'potato']

    # f.write() 코드 작성
    for w in word:
        f.write(w + ' ')