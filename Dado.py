import random
import tkinter
from tkinter import *


def bt_click():
    print('O botão foi pressionado')

    lb['text'] = f'O dado caiu no número: {random.randint(1, 6)}'


janela = tkinter.Tk()
janela.title('Dado')
bt = Button(janela, width=20, text='roll the dice.', command=bt_click)
bt.place(x=190, y=400)
lb = Label(janela, text='Welcome')
lb.place(x=220, y=0)
lb = Label(janela, text='')
lb.place(x=190, y=450)
janela.geometry('500x500+700+300')
janela.mainloop()
