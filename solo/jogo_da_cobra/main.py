import turtle
import time
import random

janela = turtle.Screen()
janela.bgcolor("#035000")
janela.title("Jogo da Cobra")
janela.setup(width=1000, height=600)
janela.tracer(0)
janela.listen()

cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape('circle')
cabeca.color("#d9ff00")
cabeca.penup()

comida = turtle.Turtle()
comida.speed(1)
comida.shape('circle')
comida.color("#ff0000")
comida.penup()
comida.goto(0, 100)

segmentos = []

def ir_para_cima():
    if cabeca.direcao != "down":
        cabeca.direcao = "up"
janela.onkeypress(ir_para_cima, "w")

def ir_para_baixo():
    if cabeca.direcao != "up":
        cabeca.direcao = "down"
janela.onkeypress(ir_para_baixo, "s")

def ir_para_direita():
    if cabeca.direcao != "left":
        cabeca.direcao = "right"
janela.onkeypress(ir_para_direita, "d")

def ir_para_esquerda():
    if cabeca.direcao != "right":
        cabeca.direcao = "left"
janela.onkeypress(ir_para_esquerda, "a")

cabeca.direcao = "stop"

def mover():
    if cabeca.direcao == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)
    elif cabeca.direcao == "down":
        y = cabeca.ycor()
        cabeca.sety(y + -20)
    elif cabeca.direcao == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)  
    elif cabeca.direcao == "left":
        x = cabeca.xcor()
        cabeca.setx(x + -20)

pontos = 0

placar = turtle.Turtle()
placar.shape('circle')
placar.color("#d9ff00")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write(f"Pontos: {pontos}", align="center", font=("Courier", 24, "normal"))

while True:

    janela.update()

    for index in range(len(segmentos) - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)

    mover()

    time.sleep(0.1)

    if cabeca.distance(comida) < 20:
        x = random.randrange(-480, 480, 20)
        y = random.randrange(-280, 280, 20)
        comida.goto(x, y)
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("circle")
        novo_segmento.color("#a3be00")
        novo_segmento.penup()
        segmentos.append(novo_segmento)
        pontos += 10
        placar.clear()
        placar.write(f"Pontos: {pontos}", align="center", font=("Courier", 24, "normal"))

    if cabeca.xcor() > 490 or cabeca.xcor() < -490 or cabeca.ycor() > 290 or cabeca.ycor() < -290:
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direcao = "stop"
        pontos = 0
        
        for segmento in segmentos:
            segmento.goto(1000, 1000)
            
        segmentos.clear()

janela.mainloop()