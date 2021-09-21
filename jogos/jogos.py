import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca (2) Adivinhação")

    valido = True
    while(valido):
        jogo = input("Qual jogo? ")
        
        
        if(check_is_digit(jogo)):
            jogo = int(jogo)
            if(jogo == 1):
                print("Jogando Forca")
                valido = False
                forca.jogar()
            elif(jogo == 2):
                print("Jogando adivinhação")
                valido = False
                adivinhacao.jogar()
            else:
                print("Jogo inválido. Disponíveis: (1) Forca (2) Adivinhacao")


def check_is_digit(jogo):
    if jogo.strip().isdigit():
        return True
    else:
        print("Digitou uma opção inválida! Disponíveis: (1) Forca (2) Adivinhacao")
        return False


if(__name__== "__main__"):
    escolhe_jogo()