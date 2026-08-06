from tkinter import *
from tkinter import ttk

cor1 = "#2e2e2e"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora Python")
janela.geometry("400x500")
janela.config(bg=cor1)

# Frames
frame_tela = Frame(
    janela,
    width=400,
    height=100,
    bg=cor3
)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(
    janela,
    width=400,
    height=450
)
frame_corpo.grid(row=1, column=0)

# Botoes
b_1 = Button(frame_corpo, text="C", width=20, height=4)
b_1.place(x=0, y=0)

janela.mainloop()