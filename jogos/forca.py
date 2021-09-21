import random
import sys

def jogar():

    imprime_mensagem_abertura()
    objeto = seleciona_objeto()
    if(check_is_digit(objeto)):
        objeto = int(objeto)
        if(objeto == 1):
            print("Jogando Forca com Frutas")
            palavra_secreta = carrega_palavra_secreta(objeto)
            letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
            print(letras_acertadas)
        elif(objeto == 2):
            print("Jogando Forca com Ferramentas de Cozinha")
            palavra_secreta = carrega_palavra_secreta(objeto)
            letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
            print(letras_acertadas)
        else:
            #print("Tema inválido.")
            sys.exit("Tema inválido.")
    else:
        sys.exit("")
            
    
   # letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
  #  print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    lista_chute = []
    lista_letras = []

    while(not enforcou and not acertou):
        chute = pede_chute()
        lista_letras.append(chute)
        if(chute in lista_chute):
            print("Você já chutou essa letra {}.".format(chute))
        else:
            if(chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas, palavra_secreta)
                print("Letras já jogadas {}".format(lista_letras))
            else:
                erros += 1
                desenha_forca(erros)
                print("Letras já jogadas {}".format(lista_letras))

            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)
        lista_chute.append(chute)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    
    print("Fim de jogo!")

def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")

def seleciona_objeto():
    print("Quer adivinhar ingredientes ou ferramentas de cozinha? ")
    return input("(1) Frutas (2) Ferramentas de cozinha ")

def check_is_digit(objeto):
    if objeto.strip().isdigit():
        return True
    else:
        print("Digitou uma opção inválida!")
        return False

def carrega_palavra_secreta(objeto):
    if(objeto == 1):
        arquivo = open("frutas.txt", "r", encoding="utf-8")
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()
    else:
        arquivo = open("ferramentas.txt", "r", encoding="utf-8")
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual letra? ")
    if(chute == ' '):
        chute = chute.upper()
    else:
        chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__== "__main__"):
    jogar()