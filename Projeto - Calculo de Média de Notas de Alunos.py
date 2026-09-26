# Inicio do Programa
print ("Bem-vindo ao Sistema de Gestão de Notas de Alunos")

# Passo 1: Adicionar notas manualmente
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

# Armazenar as notas em uma listas
notas = [nota1, nota2, nota3, nota4]

# Passo 2: Calcular Média

if notas:
    soma_notas = 0
    for nota in notas:
        soma_notas += nota
    media = soma_notas / len(notas)
else:
    media = 0

# Passo 3: Determinar Situação

if media >= 7:
    situacao = "Aprovado"
else: 
    situacao = "Reprovado"

#Passo 4: Exibir relatório final

print("\nRelatório Final")
print("Notas:", notas)
print("Média:", media)
print("Situação:", situacao)
