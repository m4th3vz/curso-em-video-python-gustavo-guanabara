''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

# Variáveis auxiliares
total_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_de_20 = 0

# Loop para 4 pessoas
for i in range(4):
    print(f"\n--- Pessoa {i + 1} ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    total_idade += idade

    if sexo == "M":
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    elif sexo == "F":
        if idade < 20:
            mulheres_menos_de_20 += 1

# Cálculo da média
media_idade = total_idade / 4

# Exibindo os resultados
print(f"\nA média de idade do grupo é de {media_idade:.1f} anos.")
print(f"O homem mais velho é {homem_mais_velho} e tem {idade_homem_mais_velho} anos.")

# Pluralização da mensagem final
if mulheres_menos_de_20 == 0:
    print("Nenhuma mulher tem menos de 20 anos.")
elif mulheres_menos_de_20 == 1:
    print("1 mulher tem menos de 20 anos.")
else:
    print(f"{mulheres_menos_de_20} mulheres têm menos de 20 anos.")
