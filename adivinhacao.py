import random

def jogar_advinhacao():
    print('##################################')
    print('Bem vindo ao jogo da adivinhação!')
    print('##################################')

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0

    print("Qual nivel de dificuldade ?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Define o Nível:"))

    pontos = 1000

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas+1):
        print('------------------------------------------------')
        print('Tentativa {} de {}'.format(rodada,total_tentativas))
        chute = int(input('Digite um numero entre 1 e 100:'))
        print('voce digitou:',chute)

        if(chute < 1 or chute > 100):
            print('Voce deve digitar um numero entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print('Voce acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Chute acima do numero!')
            elif(menor):
                print('Chute abaixo do numero!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos  = pontos - pontos_perdidos
            if(rodada == total_tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print('Fim de jogo')

if(__name__ == "__main__"):
    jogar_advinhacao()