from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry("400x500")
janela.resizable(False, False)

# Cores
cor1 = "#1E1E1E"
cor2 = "#2f2f2f"
cor3 = "#ffffff"
cor4 = "#ffb300"

# Frames
frame_cima = Frame(janela, width=400, height=180, pady=0, padx=0, relief=SOLID, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=400, height=400, pady=0, padx=0, relief=SOLID, bg=cor2)
frame_baixo.grid(row=1, column=0)

# Label frames de cima
label_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 18 bold"))
label_calculadora.place(relx=0.5, y=60, anchor=CENTER)

label_idade = Label(frame_cima, text='DE IDADE', width=25, height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor4, font=("Arial 38 bold"))
label_idade.place(relx=0.5, y=110, anchor=CENTER)

# Label frames de baixo
label_data_inicial = Label(frame_baixo, text='Data inicial', height=1, padx=0, pady=0, anchor=NW, bg=cor2, fg=cor3, font=("Ivy 11 bold"))
label_data_inicial.place(x=25, y=30)

cal_1 = DateEntry(frame_baixo, width=25, bg='darkblue', fg=cor3, borderwith=2, date_patter='DD/mm/yyyy', y=2026)
cal_1.place(x=200, y=30)

label_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, anchor=NW, bg=cor2, fg=cor3, font=("Ivy 11 bold"))
label_data_nascimento.place(x=25, y=90)

cal_2 = DateEntry(frame_baixo, width=25, bg='darkblue', fg=cor3, borderwith=2, date_patter='DD/mm/yyyy', y=2026)
cal_2.place(x=200, y=90)

janela.mainloop()