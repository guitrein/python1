import forca
import adivinhacao

print("************************")
print("*** ESCOLHA SEU JOGO ***")
print("************************")

print("(1) Forca / (2) Advinhação")
jogo = int(input("Qual jogo você escolhe?"))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando Advinhação")
    adivinhacao.jogar_advinhacao()