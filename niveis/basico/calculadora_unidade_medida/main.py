from tkinter import *
from tkinter import ttk

# Cores
cor1 = '#000000'
cor2 = '#ffffff'
cor3 = '#3b3b3b'

janela = Tk()
janela.title('')

janela.geometry('800x400')
janela.resizable(False, False)
janela.configure(bg = cor3)

# Frame janela
frame_cima = Frame(janela, width=550, height=80, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_cima.place(x=2, y=2)

janela.mainloop()