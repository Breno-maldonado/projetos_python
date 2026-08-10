from tkinter import *
from tkinter import ttk

cor1 = "#2e2e2e"
cor2 = "#ffffff"
cor3 = "#3f6969"
cor4 = "#D4D4D4"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora Python")
janela.geometry("400x500")
janela.resizable(False, False)
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

todos_valores = ""

# funcao
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # passando valor para tela
    valor_texto.set(todos_valores)

# funcao calculo
def calcular():
    resultado = eval(todos_valores)
    print(resultado)

# funcao limpar tela
def limpar_tela():
    todos_valores=""
    valor_texto.set("")

# Label
valor_texto = StringVar()

app_label = Label(
    frame_tela,
    textvariable=valor_texto,
    width=15,
    height=2,
    padx=5,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=("Ivy 32 bold"),
    bg=cor3,
    fg=cor2
)
app_label.place(x=0,y=0)

 
# Botoes C % /
b_1 = Button(frame_corpo, command=limpar_tela ,text="C", width=18, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_1.place(x=6, y=4)
b_2 = Button(frame_corpo, command=lambda:entrar_valores("%") ,text="%", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_2.place(x=206, y=4)
b_3 = Button(frame_corpo, command=lambda:entrar_valores("/") ,text="/", width=8, height=3, bg=cor5, bd=1, fg=cor2, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_3.place(x=306, y=4)

# Botoes 7 8 9 *
b_4 = Button(frame_corpo, command=lambda:entrar_valores("7") ,text="7", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_4.place(x=6, y=80)
b_5 = Button(frame_corpo, command=lambda:entrar_valores("8") ,text="8", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_5.place(x=106, y=80)
b_6 = Button(frame_corpo, command=lambda:entrar_valores("9") ,text="9", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_6.place(x=206, y=80)
b_7 = Button(frame_corpo, command=lambda:entrar_valores("*") ,text="*", width=8, height=3, bg=cor5, bd=1, fg=cor2, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_7.place(x=306, y=80)

# Botoes 4 5 6 -
b_8 = Button(frame_corpo, command=lambda:entrar_valores("4") ,text="4", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_8.place(x=6, y=160)
b_9 = Button(frame_corpo, command=lambda:entrar_valores("5") ,text="5", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_9.place(x=106, y=160)
b_10 = Button(frame_corpo, command=lambda:entrar_valores("6") ,text="6", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_10.place(x=206, y=160)
b_11 = Button(frame_corpo, command=lambda:entrar_valores("-") ,text="-", width=8, height=3, bg=cor5, bd=1, fg=cor2, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_11.place(x=306, y=160)

# Botoes 1 2 3 +
b_12 = Button(frame_corpo, command=lambda:entrar_valores("1") ,text="1", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_12.place(x=6, y=240)
b_13 = Button(frame_corpo, command=lambda:entrar_valores("2") ,text="2", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_13.place(x=106, y=240)
b_14 = Button(frame_corpo, command=lambda:entrar_valores("3") ,text="3", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_14.place(x=206, y=240)
b_15 = Button(frame_corpo, command=lambda:entrar_valores("+") ,text="+", width=8, height=3, bg=cor5, bd=1, fg=cor2, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_15.place(x=306, y=240)

# Botoes 0 . =
b_16 = Button(frame_corpo, command=lambda:entrar_valores("0") ,text="0", width=18, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_16.place(x=6, y=320)
b_17 = Button(frame_corpo, command=lambda:entrar_valores(".") ,text=".", width=8, height=3, bg=cor4, bd=1, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_17.place(x=206, y=320)
b_18 = Button(frame_corpo, command=calcular ,text="=", width=8, height=3, bg=cor5, bd=1, fg=cor2, font=("Ivy 13 bold"), relief=SOLID, overrelief=RIDGE)
b_18.place(x=306, y=320)


janela.mainloop()
