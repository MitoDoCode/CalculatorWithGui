from tkinter import *

def button_press(num):
    global equationTxt
    equationTxt += str(num)
    equationLabel.set(equationTxt)

def equals():
    global equationTxt
    try:
        total = str(eval(equationTxt))
        equationLabel.set(total)
        equationTxt = total
    except Exception as e:
        equationLabel.set("Error")
        equationTxt = ""

def clear():
    global equationTxt
    equationTxt = ""
    equationLabel.set("")

def backspace():
    global equationTxt
    equationTxt = equationTxt[:-1]
    equationLabel.set(equationTxt)

window = Tk()
window.title("Basic Calculator GUI")
window.geometry("400x700")
window.resizable(False,False)

Icon = PhotoImage(file='DDLC.png')
window.iconphoto(True,Icon)

#photo used here is not mine credits to their owner


equationTxt = ""
equationLabel = StringVar()

label = Label(window, textvariable=equationLabel,
              font=('Arial', 25),
              bg="white",
              fg='black',
              padx=20,
              pady=10,
              width=35,
              height=4)

label.pack()

frame = Frame(window)
frame.pack()


buttons = [
    (7, 0, 0), (8, 0, 1), (9, 0, 2),
    (4, 1, 0), (5, 1, 1), (6, 1, 2),
    (1, 2, 0), (2, 2, 1), (3, 2, 2),
    (0, 3, 1)
]

for (num, row, col) in buttons:
    button = Button(frame, text=num, height=5, width=10, font=40, command=lambda n=num: button_press(n))
    button.grid(row=row, column=col)


operations = [
    ('+', 0, 3), ('-', 1, 3),
    ('*', 2, 3), ('/', 3, 3)
]

for (op, row, col) in operations:
    button = Button(frame, text=op, height=5, width=10, font=40, command=lambda o=op: button_press(o))
    button.grid(row=row, column=col)


backspace_button = Button(frame, text='=', height=5, width=10, font=40, command=equals)

backspace_button.grid(row=3, column=2)

clear_button = Button(frame, text='C', height=5, width=10, font=40, command=clear)
clear_button.grid(row=3, column=0)

equal_button = Button(frame, text='⌫', height=5, width=35, font=40, command=backspace)

backspace_button
equal_button.grid(row=4, column=0,columnspan=4)

window.mainloop()
