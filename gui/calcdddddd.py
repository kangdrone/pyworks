from tkinter import *


def click1():
    display.insert(END, '1')

def click2():
    display.insert(END, '2')


root = Tk()
root.title("나의 계산기")
root.geometry("250x150+300+200")
frame = Frame(root)
frame.pack()


display = Text(frame, width=20, height=1)   # 출력 상자
display.grid(row=0, column=0)

Button(frame, text="1", width=10, command=click1).grid(row=1, column=0)
Button(frame, text="2", width=10, command=click2).grid(row=2, column=0)


root.mainloop()