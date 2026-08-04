import tkinter as tk
from tkinter import *

class Cronometro:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronometro Python")
        self.janela.geometry("700x500")
        self.janela.minsize(500, 400)
        self.janela.maxsize(800, 600)
        self.janela.resizable(True, True)
        self.janela.configure(bg="#101010")

        # Variaveis de estado
        self.tempo_atual = "00:00:00"
        self.segundos = 0
        self.rodando = False
        self.timer_id = None

        self.criar_interface()

    def criar_interface(self):
        # Container principal
        container = Frame(self.janela, bg="#151515")
        container.pack(expand=True, fill=BOTH, padx=30, pady=30)

        # Card Principal
        card = Frame(container, bg="#151515", relief="solid", bd=4)
        card.pack(expand=True, fill=BOTH)

        # Titulo
        titulo = Label(
            card,
            text="⏱️ Cronômetro",
            font=("Arial", 12, "bold"),
            bg="#151515",
            fg="#ffffff",
        )
        titulo.pack(pady=(20, 5))

        # Tempo
        self.display = Label(
            card,
            text=self.tempo_atual,
            font=("Arial", 48, "bold"),
            bg="#151515",
            fg="#5100ff",
        )
        self.display.pack(pady=15)

        # Frame dos botoes
        frame_botoes = Frame(card, bg="#151515")
        frame_botoes.pack(pady=20)

        # Botao iniciar
        self.btn_iniciar = Button(
            frame_botoes,
            command=self.iniciar,
            text="Iniciar",
            font=("Arial", 10, "bold"),
            bg="#353535",
            fg="#00ff1e",
            padx=20,
            pady=8,
            relief="solid",
            bd=2,
            width=10,
        )
        self.btn_iniciar.grid(row=0, column=0, padx=5)

        # Botao Pausar
        self.btn_pausar = Button(
            frame_botoes,
            command=self.pausar,
            text="Pausar",
            font=("Arial", 10, "bold"),
            bg="#353535",
            fg="#ff0000",
            padx=20,
            pady=8,
            relief="solid",
            bd=2,
            width=10,
        )
        self.btn_pausar.grid(row=0, column=1, padx=5)

        # Botao Resetar
        self.btn_resetar = Button(
            frame_botoes,
            command=self.resetar,
            text="Resetar",
            font=("Arial", 10, "bold"),
            bg="#353535",
            fg="#00d0ff",
            padx=20,
            pady=8,
            relief="solid",
            bd=2,
            width=10,
        )
        self.btn_resetar.grid(row=0, column=2, padx=5)

    def atualizar_tempo(self):
        if self.rodando:
            self.segundos += 1
            horas = self.segundos // 3600
            minutos = (self.segundos % 3600) // 60
            segundos = self.segundos % 60

            self.tempo_atual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.display.config(text=self.tempo_atual)

            # Chama novamente apos 1 segundo
            self.timer_id = self.janela.after(1000, self.atualizar_tempo)

    def iniciar(self):
        # CORRIGIDO: usa self.rodando em vez de self.btn.rodando
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()

    def pausar(self):
        if self.rodando:
            self.rodando = False
            if self.timer_id:
                self.janela.after_cancel(self.timer_id)

    def resetar(self):
        self.pausar()
        self.segundos = 0
        self.tempo_atual = "00:00:00"
        self.display.config(text=self.tempo_atual)

if __name__ == "__main__":
    janela = Tk()
    app = Cronometro(janela)
    janela.mainloop()