import random
import time

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(1, self.ataque - alvo.defesa + random.randint(-2, 2))
        alvo.vida -= dano
        print(f"⚔️ {self.nome} atacou {alvo.nome} causando {dano} de dano!")

    def esta_vivo(self):
        return self.vida > 0


class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=15, defesa=5)
        self.nivel = 1
        self.exp = 0

    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        print(f"✨ Você ganhou {quantidade} de EXP!")

        if self.exp >= self.nivel * 50:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.exp = 0
        self.vida_max += 20
        self.ataque += 5
        self.defesa += 2
        self.vida = self.vida_max

        print(f"\n🔥 LEVEL UP! Você agora é nível {self.nivel}")
        print("❤️ Vida aumentou")
        print("⚔️ Ataque aumentou")
        print("🛡️ Defesa aumentou\n")

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2 + random.randint(0, 5)
        alvo.vida -= dano
        print(f"💥 {self.nome} usou GOLPE ESPECIAL causando {dano} de dano!")


class Inimigo(Personagem):
    def __init__(self, nivel):
        nomes = ["Goblin", "Esqueleto", "Orc", "Bandido"]
        nome = random.choice(nomes)

        vida = 60 + nivel * 15
        ataque = 10 + nivel * 3
        defesa = 3 + nivel

        super().__init__(nome, vida, ataque, defesa)


def batalha(jogador, inimigo):
    print(f"\n⚠️ Um {inimigo.nome} apareceu!")
    time.sleep(1)

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print("\n--- STATUS ---")
        print(f"{jogador.nome} ❤️ {jogador.vida}/{jogador.vida_max}")
        print(f"{inimigo.nome} ❤️ {inimigo.vida}\n")

        print("1 - Atacar")
        print("2 - Habilidade Especial")
        print("3 - Defender")

        escolha = input("Escolha sua ação: ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            jogador.habilidade_especial(inimigo)
        elif escolha == "3":
            print("🛡️ Você se defendeu! Defesa aumentada neste turno.")
            jogador.defesa += 3
        else:
            print("❌ Ação inválida!")
            continue

        if inimigo.esta_vivo():
            time.sleep(1)
            inimigo.atacar(jogador)

        if escolha == "3":
            jogador.defesa -= 3

        time.sleep(1)

    if jogador.esta_vivo():
        print(f"\n🏆 Você derrotou o {inimigo.nome}!")
        jogador.ganhar_exp(30)
    else:
        print("\n💀 Você foi derrotado... GAME OVER")
        exit()


def jogo():
    print("🗡️ RPG DE BATALHA 🗡️")
    nome = input("Digite o nome do herói: ")

    jogador = Jogador(nome)

    while True:
        inimigo = Inimigo(jogador.nivel)
        batalha(jogador, inimigo)

        continuar = input("\nDeseja lutar novamente? (s/n): ").lower()
        if continuar != "s":
            print("👋 Obrigado por jogar!")
            break


jogo()