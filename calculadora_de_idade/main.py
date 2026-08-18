from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

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

# Calculo de idade
def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    # Formato data
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1, mes_1, dia_1)

    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    label_ano['text'] = anos
    label_mes['text'] = meses
    label_dia['text'] = dias

# Label frames de baixo
label_data_inicial = Label(frame_baixo, text='Data hoje', height=1, padx=0, pady=0, anchor=NW, bg=cor2, fg=cor3, font=("Ivy 11 bold"))
label_data_inicial.place(x=25, y=30)

cal_1 = DateEntry(frame_baixo, width=25, bg='darkblue', fg=cor3, borderwith=2, date_pattern='mm/dd/y', y=2026)
cal_1.place(x=200, y=30)

label_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, anchor=NW, bg=cor2, fg=cor3, font=("Ivy 11 bold"))
label_data_nascimento.place(x=25, y=90)

cal_2 = DateEntry(frame_baixo, width=25, bg='darkblue', fg=cor3, borderwith=2, date_pattern='mm/dd/y', y=2026)
cal_2.place(x=200, y=90)

# Label ano, mes e dia
label_ano = Label(frame_baixo, text='--', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 25 bold"))
label_ano.place(x=80, y=220)
label_ano_nome = Label(frame_baixo, text='Anos', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 11 bold"))
label_ano_nome.place(x=80, y=280)

label_mes = Label(frame_baixo, text='--', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 25 bold"))
label_mes.place(x=180, y=220)
label_mes_nome = Label(frame_baixo, text='Meses', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 11 bold"))
label_mes_nome.place(x=175, y=280)

label_dia = Label(frame_baixo, text='--', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 25 bold"))
label_dia.place(x=280, y=220)
label_dia_nome = Label(frame_baixo, text='Dias', height=1, padx=3, anchor=CENTER, bg=cor1, fg=cor3, font=("Ivy 11 bold"))
label_dia_nome.place(x=282, y=280)

# Botão calcular
b_calcular = Button(frame_baixo, command=calcular ,text='CALCULAR', width=20, height=1, bg=cor4, fg=cor1, font=("Arial 12 bold"), relief=SOLID, overrelief=RIDGE)
b_calcular.place(x=99, y=150)

janela.mainloop()