print("##############################################")
print("            Manuseio de Listas                ")
print("##############################################")

nome = input("Digite seu nome: ")

lista = [2, 5, 4, 7, 2, 1, 9]

print("********************************************************************")
print("Olá", nome, "! Aqui está sua lista:")
print(lista)
print("********************************************************************")

x = int(input("Digite 1 para adicionar e 2 para remover itens na lista: "))

if x == 1:
    adicionar = int(input("Digite o número que deseja adicionar: "))
    lista.append(adicionar)
    print("Item adicionado com sucesso!")

elif x == 2:
    remover = int(input("Digite o número que deseja remover: "))
    if remover in lista:
        lista.remove(remover)
        print("Item removido com sucesso!")
    else:
        print("O número", remover, "não está na lista!")

else:
    print("Opção inválida! Digite apenas 1 ou 2.")

print("********************************************************")
print("Lista modificada:")
print(lista)
