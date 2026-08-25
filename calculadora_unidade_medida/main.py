from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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
janela.configure(bg=cor5)

# Frame janela cima
frame_cima = Frame(janela, width=550, height=75, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_cima.place(x=5, y=5)

# Janela esquerda
frame_esquerda = Frame(janela, width=550, height=310, bg=cor2, pady=0, padx=3, relief=SOLID)
frame_esquerda.place(x=5, y=85)

# IMPEDE que o frame encolha e FORÇA a distribuição do tamanho fixo entre os botões
frame_esquerda.grid_propagate(False)

for i in range(3):
    frame_esquerda.grid_columnconfigure(i, weight=1)
    frame_esquerda.grid_rowconfigure(i, weight=1)

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
# Massa
img_0 = Image.open('images/icons8-balança-50.png')
img_0 = img_0.resize((40, 40), Image.Resampling.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text='MASSA', image=img_0, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Tempo
img_1 = Image.open('images/icons8-cronômetro-50.png')
img_1 = img_1.resize((40, 40), Image.Resampling.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, text='TEMPO', image=img_1, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Comprimento
img_2 = Image.open('images/icons8-régua-50.png')
img_2 = img_2.resize((40, 40), Image.Resampling.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, text='COMPRIMENTO', image=img_2, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Area
img_3 = Image.open('images/icons8-medir-50.png')
img_3 = img_3.resize((40, 40), Image.Resampling.LANCZOS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text='AREA', image=img_3, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

# Quantidade
img_4 = Image.open('images/icons8-pluviômetro-50.png')
img_4 = img_4.resize((40, 40), Image.Resampling.LANCZOS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_esquerda, text='QUANTIDADE', image=img_4, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

# Velocidade
img_5 = Image.open('images/icons8-velocímetro-50.png')
img_5 = img_5.resize((40, 40), Image.Resampling.LANCZOS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_esquerda, text='VELOCIDADE', image=img_5, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

# Temperatura
img_6 = Image.open('images/icons8-termômetro-médico-50.png')
img_6 = img_6.resize((40, 40), Image.Resampling.LANCZOS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_esquerda, text='TEMPERATURA', image=img_6, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

# Energia
img_7 = Image.open('images/icons8-energia-48.png')
img_7 = img_7.resize((40, 40), Image.Resampling.LANCZOS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_esquerda, text='ENERGIA', image=img_7, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

# Pressão
img_8 = Image.open('images/icons8-pressão-50.png')
img_8 = img_8.resize((40, 40), Image.Resampling.LANCZOS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_esquerda, text='PRESSÃO', image=img_8, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)

# Config frame direita
l_unidade_nome = Label(frame_direita, text='UNIDADE',width=16, height=3, padx=0, relief=GROOVE, anchor=CENTER, font=('Ivy 18 bold'), fg=cor4, bg=cor2)
l_unidade_nome.place(x=-4, y=-9)

janela.mainloop()