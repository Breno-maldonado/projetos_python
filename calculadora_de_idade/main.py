from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry("400x500")
janela.resizable(False, False)

# Cores
cor1 = "#1E1E1E"
cor2 = "#2f2f2f"

# Frames
frame_cima = Frame(janela, width=400, height=180, pady=0, padx=0, relief=SOLID, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=400, height=400, pady=0, padx=0, relief=SOLID, bg=cor2)
frame_baixo.grid(row=1, column=0)

# Label frames de cima
label_calculadora = Label(frame_cima, text='Calculadora de Idade', width=25, height=1, padx=3, relief=SOLID, anchor=CENTER, bg=cor2, font=("Ivy 13 bold"))
label_calculadora.place(relx=0.5, y=40, anchor=CENTER)

janela.mainloop()