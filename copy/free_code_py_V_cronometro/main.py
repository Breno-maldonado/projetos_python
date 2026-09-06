import time
import os

print("""
░█████╗░██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗████████╗██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██████╔╝██║░░██║██╔██╗██║██║░░██║██╔████╔██║█████╗░░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══██╗██║░░██║██║╚████║██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝██║░░██║╚█████╔╝██║░╚███║╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\n""")

tempo = int(input("Digite quanto tempo você deseja cronometrar (em segundos): "))
print("\nIniciando contagem regressiva...\n")

try:
    for i in range(tempo, -1, -1):
        segundos = i % 60
        minutos = int(i / 60) % 60
        horas = int(i / 3600)
        
        print(f"\rTempo restante -> {horas:02}:{minutos:02}:{segundos:02}", end="", flush=True)
        
        time.sleep(1)

    print("\n\nO tempo acabou!")

except KeyboardInterrupt:
    print("\n\nCronômetro interrompido pelo usuário.")