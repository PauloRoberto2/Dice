import random
import tkinter
from tkinter import *


def bt_click():
    print('The button was pressed')

    lb['text'] = f'The number chosen was: {random.randint(1, 6)}'


janela = tkinter.Tk()
janela.title('Dice')
bt = Button(janela, width=20, text='Roll the dice', command=bt_click)
bt.place(x=190, y=400)
lb = Label(janela, text='Welcome')
lb.place(x=220, y=0)
lb = Label(janela, text='')
lb.place(x=190, y=450)
janela.geometry('500x500+700+300')
janela.mainloop()
