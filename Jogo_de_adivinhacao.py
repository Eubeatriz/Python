import random 

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")


numero_secreto = round(random.randrange(1,101))
total_tentativas = 3
rodada = 1
pontos = 1000

#######################################################################################################################

print("Qual nível de dificuldade deseja?")
print("(1) Fácil (2) Médio (3) Difícil")

dificuldade = int(input("Defina o nível: "))
print("*********************************")
if dificuldade == 1:
    total_tentativas = 10
    
elif dificuldade == 2:
    total_tentativas = 5
    
elif dificuldade == 3:
    total_tentativas = 3

else:
    print("Nivel de dificuldade não existente!")
    

for rodada in range (1,total_tentativas + 1):
    print("|Tentativa {} de {}|". format(rodada, total_tentativas))
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou " , chute)
    
    if(chute > 100) or (chute < 1):
        print("**********************************************")
        print("Você só pode digitar números de 1 a 100!")
        print("**********************************************")
        continue
        
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("<<<O seu chute foi MAIOR do que o número secreto!>>>")
            print("**********************************************")
        elif(menor):
            print("<<<O seu chute foi MENOR do que o número secreto!>>>")
            print("**********************************************")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
####################################################################################################################### 

print("O número secreto era","<<<", numero_secreto, ">>>")  
print("Sua pontuação foi...","<<<", pontos, ">>>")
print("Fim do jogo!")
            print("**********************************************")
#######################################################################################################################    
print("O número secreto era", numero_secreto)   
print("Fim do jogo")
