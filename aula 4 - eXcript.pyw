from tkinter import *

def bt_click():
    print('bt_click')
    lb['text'] = 'Funcionou!'

janela = Tk()

bt = Button(janela, width=20, text='Ok', command=bt_click)
bt.place(x=100,y=100)

lb = Label(janela, text='Texte')
lb.place(x=100,y=150)

janela.geometry('300x200+800+500')
janela.mainloop()
