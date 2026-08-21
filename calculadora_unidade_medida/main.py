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

# Frame janela cima
frame_cima = Frame(janela, width=550, height=75, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_cima.place(x=5, y=5)
# Janela esquerda
frame_esquerda = Frame(janela, width=550, height=310, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_esquerda.place(x=5, y=85)
# Janela direita
frame_direita = Frame(janela, width=232, height=390, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_direita.place(x=561, y=5)

# Tema janela
estilo = ttk.Style(janela)
estilo.theme_use("clam")

janela.mainloop()