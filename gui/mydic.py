# 방향 - W(west), E(east), S(south), N(north)
from tkinter import *

def click():
    try:
        word = entry.get()             # 입력된 데이터를 가져와서
        definition = dic[word]         # 단어로 정의를 검색
        text.delete(0.0, END)
        text.insert(END, definition)   # 정의 출력상자에 넣음
    except KeyError:
        text.delete(0.0, END)
        text.insert(END, "단어의 정의를 찾을 수 없습니다.")

root = Tk()
root.title("용어 사전")

Label(root, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요").grid(row=0, column=0, sticky=W)
entry = Entry(root, width=20, bg="lightgreen")
entry.grid(row=1, column=0, sticky=W)
Button(root, text="제출", command=click).grid(row=2, column=0, sticky=W)
Label(root, text="정의 : ").grid(row=3, column=0, sticky=W)
text = Text(root, width=80, height=8, bg="lightgreen")
text.grid(row=4, column=0, sticky=W)

dic = {
    "이진수" : "2진법으로 나타낸 숫자, 0과 1로 구성됨",
    "html" : "하이퍼텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.",
    "함수" : "재사용 가능한 코드 조각이며, function 이라고도 한다.",
    "버그" : "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각이다."
}


root.mainloop()