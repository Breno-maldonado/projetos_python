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
      fg="#ffffff"
    )
    titulo.pack(pady=(20,5))


if __name__ == "__main__":
  janela = Tk()
  app = Cronometro(janela)
  janela.mainloop()