from tkinter import *

class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="deg C").grid(row=0, column=0)
        Button(frame, text="변환").grid(row=0, column=0)


root = Tk()
root.title("Temp Converter")
app = App(root)

root.mainloop()