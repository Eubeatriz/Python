import random 

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")


numero_secreto = round(random.randrange(1,101))
total_tentativas = 3
rodada = 1

#######################################################################################################################
for rodada in range (1,4):
    print("Tentativa {} de {}". format(rodada, total_tentativas))
    chute = int(input("Digite o seu número entre 1 e 100:"))
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
        print("Parabêns! Você acertou!")
        break
    else:
        if(maior):
            print("**********************************************")
            print("O seu chute foi maior do que o número secreto!")
            print("**********************************************")
        elif(menor):
            print("**********************************************")
            print("O seu chute foi menor do que o número secreto!")
            print("**********************************************")
#######################################################################################################################    
print("O número secreto era", numero_secreto)   
print("Fim do jogo")
