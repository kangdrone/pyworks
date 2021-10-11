from tkinter import *

class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="deg C").grid(row=0, column=0)
        Button(frame, text="변환", command=self.convert).grid(row=1, columnspan=2)

    def convert(self):
        print("아직 구현되지 않음")

root = Tk()
root.title("Temp Converter")
root.geometry("250x60+200+200")
app = App(root)

root.mainloop()