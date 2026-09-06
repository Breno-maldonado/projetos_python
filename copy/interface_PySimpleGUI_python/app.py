import PySimpleGUI as sg

sg.theme("Reddit")

FONTE_CORPO = ("Segoe UI", 11)
FONTE_TITULO = ("Segoe UI", 16, "bold")

layout = [
    [sg.VPush()],

    [sg.Text("LOGIN", font=FONTE_TITULO, pad=(0, 20))],

    [sg.Text("Usuário:", size=(8, 1), font=FONTE_CORPO), 
     sg.Input(key="usuario", size=(25, 1))],

    [sg.Text("Senha:", size=(8, 1), font=FONTE_CORPO), 
     sg.Input(key="senha", password_char="*", size=(25, 1))],

    [sg.Checkbox("Manter conectado", font=("Segoe UI", 9), pad=(0, 20))],

    [sg.Button("ENTRAR", size=(20, 1), button_color=("white", "#0078D7"), 
               font=("Segoe UI", 11, "bold"), border_width=0)],
    [sg.VPush()]
]

janela = sg.Window("Sistema de Login", layout, size=(400, 350), 
                   element_justification='center', finalize=True)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == "Entrar":
        print(f"Tentando login com: {valores['usuario']}")
    if valores["usuario"] == "admin" and valores["senha"] == "0000":
        sg.popup("Sucesso!")
    else:
        sg.popup_error("Usuário ou senha incorretos")

janela.close()