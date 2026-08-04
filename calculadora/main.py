from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora Python")
janela.geometry("400x500")

frame_tela = Frame(
    janela,
    width=400,
    height=50,
    bg="#2e2e2e"
)
frame_tela.grid(row=0, column=0)

janela.mainloop()