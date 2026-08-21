from tkinter import *
from tkinter import ttk

# Cores
cor1 = '#000000'
cor2 = '#ffffff'
cor3 = '#3b3b3b'
cor4 = "#ff002b"
cor5 = "#ff2600"


janela = Tk()
janela.title('')

janela.geometry('800x400')
janela.resizable(False, False)
janela.configure(bg = cor5)

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

# Config frame cima
l_app_nome = Label(frame_cima, text='CALCULADORA DE UNIDADES DE MEDIDAS', height=1, padx=0, relief=FLAT, anchor=CENTER, font=('Ivy 18 bold'), fg=cor4, bg=cor2)
l_app_nome.place(x=10, y=20)

# Config frame esquerda
b_0 = Button(frame_esquerda, text='PESO',width=10, height=2, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 13 bold'), fg=cor4, bg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

janela.mainloop()