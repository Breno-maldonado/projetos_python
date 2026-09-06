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

# Config funcionalidade
unidades = {
    'massa': [
        {'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1},
        {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}
    ],
    'tempo': [
        {'ano': 31536000}, {'mes': 2592000}, {'semana': 604800},
        {'dia': 86400}, {'h': 3600}, {'min': 60}, {'s': 1}, {'ms': 0.001}
    ],
    'comprimento': [
        {'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1},
        {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}
    ],
    'area': [
        {'km²': 1000000}, {'hm²': 10000}, {'dam²': 100}, {'m²': 1},
        {'dm²': 0.01}, {'cm²': 0.0001}, {'mm²': 0.000001}
    ],
    'quantidade': [
        {'m³': 1000}, {'l': 1}, {'dl': 0.1}, {'cl': 0.01}, {'ml': 0.001}
    ],
    'velocidade': [
        {'km/h': 1}, {'m/s': 3.6}, {'mph': 1.60934}, {'nó': 1.852}
    ],
    'temperatura': [
        {'C': 'Celsius'}, {'F': 'Fahrenheit'}, {'K': 'Kelvin'}
    ],
    'energia': [
        {'kJ': 1000}, {'J': 1}, {'kcal': 4184}, {'cal': 4.184},
        {'kWh': 3600000}, {'eV': 1.60218e-19}
    ],
    'pressao': [
        {'bar': 100000}, {'atm': 101325}, {'Pa': 1}, {'kPa': 1000},
        {'mmHg': 133.322}, {'psi': 6894.76}
    ],
}

categoria_atual = ''

def mostrar_menu(i):
    global categoria_atual
    categoria_atual = i

    unidades_lista = []
    for d in unidades[i]:
        unidades_lista.extend(d.keys())

    c_de['values'] = unidades_lista
    c_para['values'] = unidades_lista

    if unidades_lista:
        c_de.set(unidades_lista[0])
        c_para.set(unidades_lista[1] if len(unidades_lista) > 1 else unidades_lista[0])

    l_unidade_nome['text'] = i.upper()

def calcular():
    if not categoria_atual:
        l_resultado['text'] = 'Erro'
        return

    try:
        valor = float(e_numero.get())
        unid_de = c_de.get()
        unid_para = c_para.get()
    except ValueError:
        l_resultado['text'] = 'Invalido'
        return

    # Tratamento para Temperatura
    if categoria_atual == 'temperatura':
        if unid_de == unid_para:
            res = valor
        elif unid_de == 'C' and unid_para == 'F':
            res = (valor * 9/5) + 32
        elif unid_de == 'C' and unid_para == 'K':
            res = valor + 273.15
        elif unid_de == 'F' and unid_para == 'C':
            res = (valor - 32) * 5/9
        elif unid_de == 'F' and unid_para == 'K':
            res = (valor - 32) * 5/9 + 273.15
        elif unid_de == 'K' and unid_para == 'C':
            res = valor - 273.15
        elif unid_de == 'K' and unid_para == 'F':
            res = (valor - 273.15) * 9/5 + 32
    else:
        # Busca dos fatores de conversão
        fator_de = None
        fator_para = None

        for item in unidades[categoria_atual]:
            if unid_de in item:
                fator_de = item[unid_de]
            if unid_para in item:
                fator_para = item[unid_para]

        if fator_de is not None and fator_para is not None:
            # Converte primeiro para a unidade base e depois para a unidade de destino
            valor_base = valor * fator_de
            res = valor_base / fator_para
        else:
            res = 0

    # Formatação do resultado para exibição
    if abs(res) < 0.0001 and res != 0:
        l_resultado['text'] = f"{res:.2e}"
    else:
        l_resultado['text'] = f"{res:.4g}"

# Config frame direita
l_unidade_nome = Label(frame_direita, text='UNIDADE', width=16, height=3, padx=0, relief=GROOVE, anchor=CENTER, font=('Ivy 18 bold'), fg=cor1, bg=cor2)
l_unidade_nome.place(x=-4, y=-9)

l_de = Label(frame_direita, text='De', height=1, padx=3, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), fg=cor1, bg=cor2)
l_de.place(x=10, y=120)
c_de = ttk.Combobox(frame_direita, width=5, justify=CENTER, font=('Ivy 10 bold'))
c_de.place(x=40, y=120)

l_para = Label(frame_direita, text='Para', height=1, padx=3, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), fg=cor1, bg=cor2)
l_para.place(x=120, y=120)
c_para = ttk.Combobox(frame_direita, width=5, justify=CENTER, font=('Ivy 10 bold'))
c_para.place(x=160, y=120)

l_info = Label(frame_direita, text='Digite o número', width=16, height=2, padx=5, pady=3, relief=FLAT, anchor=CENTER, font=('Ivy 10 bold'), fg=cor1, bg=cor2)
l_info.place(x=50, y=200)

e_numero = Entry(frame_direita, width=9, font=('Ivy 14'), justify=CENTER, relief=SOLID)
e_numero.place(x=12, y=251)

b_c = Button(frame_direita, command=calcular, text='CALCULAR', relief=SOLID, anchor=CENTER, font=('Arial 10 bold'), fg=cor2, bg=cor4)
b_c.place(x=130, y=250)

l_resultado = Label(frame_direita, text='0', width=10, height=1, padx=3, pady=2, relief=GROOVE, anchor=CENTER, font=('Ivy 18 bold'), fg=cor1, bg=cor2)
l_resultado.place(x=33, y=320)

# Config frame esquerda
# Massa
img_0 = Image.open('images/icons8-balança-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, command=lambda: mostrar_menu('massa'), text='MASSA', image=img_0, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Tempo
img_1 = Image.open('images/icons8-cronômetro-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, command=lambda: mostrar_menu('tempo'), text='TEMPO', image=img_1, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Comprimento
img_2 = Image.open('images/icons8-régua-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, command=lambda: mostrar_menu('comprimento'), text='COMPRIMENTO', image=img_2, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Area
img_3 = Image.open('images/icons8-medir-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, command=lambda: mostrar_menu('area'), text='AREA', image=img_3, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

# Quantidade
img_4 = Image.open('images/icons8-pluviômetro-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_esquerda, command=lambda: mostrar_menu('quantidade'), text='QUANTIDADE', image=img_4, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

# Velocidade
img_5 = Image.open('images/icons8-velocímetro-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_esquerda, command=lambda: mostrar_menu('velocidade'), text='VELOCIDADE', image=img_5, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

# Temperatura
img_6 = Image.open('images/icons8-termômetro-médico-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_esquerda, command=lambda: mostrar_menu('temperatura'), text='TEMPERATURA', image=img_6, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

# Energia
img_7 = Image.open('images/icons8-energia-48.png').resize((40, 40), Image.Resampling.LANCZOS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_esquerda, command=lambda: mostrar_menu('energia'), text='ENERGIA', image=img_7, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

# Pressão
img_8 = Image.open('images/icons8-pressão-50.png').resize((40, 40), Image.Resampling.LANCZOS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_esquerda, command=lambda: mostrar_menu('pressao'), text='PRESSÃO', image=img_8, compound=TOP, relief=FLAT, overrelief=SOLID, anchor=CENTER, font=('Ivy 10 bold'), fg=cor4, bg=cor2)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)

# Inicializa o menu com 'massa' por padrão
mostrar_menu('massa')

janela.mainloop()