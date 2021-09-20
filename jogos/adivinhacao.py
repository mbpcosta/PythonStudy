import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    #while(rodada <= tentativas):
    for rodada in range(1,tentativas+1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior): 
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada += 1


    print("Fim.")

if(__name__== "__main__"):
    jogar()