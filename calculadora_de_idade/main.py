from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry("400x500")
janela.resizable(False, False)

# Cores
cor1 = "#2e2e2e"
cor2 = "#ffffff"
cor3 = "#3f6969"
cor4 = "#D4D4D4"
cor5 = "#FFAB40"

# Frames
frame_cima = Frame(janela, width=400, height=180, pady=0, padx=0, relief=SOLID, bg=cor1)
frame_cima.grid(row=0, column=0)

janela.mainloop()