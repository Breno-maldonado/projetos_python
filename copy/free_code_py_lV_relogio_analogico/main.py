import tkinter as tk
import time
import math

class relogio:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio Analógico")

        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack(expand=True, fill='both')
        
        self.centro_x = 200
        self.centro_y = 200
        self.raio = 150
        
        self.atualizar_relogio()

    def desenhar_face(self):
            self.canvas.delete("all")
            self.canvas.create_oval(self.centro_x - self.raio, self.centro_y - self.raio,
                                    self.centro_x + self.raio, self.centro_y + self.raio, width=4)
            
            for i in range(12):
                        angulo = math.radians(i * 30)
                        x1 = self.centro_x + (self.raio - 10) * math.sin(angulo)
                        y1 = self.centro_y - (self.raio - 10) * math.cos(angulo)
                        x2 = self.centro_x + (self.raio) * math.sin(angulo)
                        y2 = self.centro_y - (self.raio) * math.cos(angulo)
                        self.canvas.create_line(x1, y1, x2, y2, width=3)

    def desenhar_ponteiro(self, angulo, comprimento, largura, cor):
        angulo_rad = math.radians(angulo)
        x_fim = self.centro_x + comprimento * math.sin(angulo_rad)
        y_fim = self.centro_y - comprimento * math.cos(angulo_rad)
        self.canvas.create_line(self.centro_x, self.centro_y, x_fim, y_fim, width=largura, fill=cor, capstyle='round')

    def atualizar_relogio(self):
        self.desenhar_face()
        
        tempo_atual = time.localtime()
        horas = tempo_atual.tm_hour % 12
        minutos = tempo_atual.tm_min
        segundos = tempo_atual.tm_sec
        
        angulo_seg = segundos * 6          
        angulo_min = minutos * 6 + segundos * 0.1
        angulo_hora = horas * 30 + minutos * 0.5
        
        self.desenhar_ponteiro(angulo_hora, self.raio * 0.5, 6, "black")
        self.desenhar_ponteiro(angulo_min, self.raio * 0.8, 4, "blue")
        self.desenhar_ponteiro(angulo_seg, self.raio * 0.9, 2, "red")
        
        self.root.after(1000, self.atualizar_relogio)

if __name__ == "__main__":
    janela = tk.Tk()
    app = relogio(janela)
    janela.mainloop()