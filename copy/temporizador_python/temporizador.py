import time

tempo = input("Digite o tempo (em segunso): ")

if tempo.isdigit():
    tempo = int(tempo)
else:
    print("Entrada inválida!")
    quit()

while tempo:
    minutos, segundos = divmod(tempo, 60)
    timer = "{:02d}:{}".format(minutos, segundos)
    print(timer, end="\r")
    time.sleep(1)
    tempo = tempo - 1

print("O tempo acabou!")