''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

# Inicializa as variáveis de maior e menor peso
maior_peso = 0
menor_peso = 0

# Laço para ler 5 pesos
for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))

    # Na primeira iteração, define o primeiro peso como maior e menor
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        # Atualiza o maior peso, se necessário
        if peso > maior_peso:
            maior_peso = peso
        # Atualiza o menor peso, se necessário
        if peso < menor_peso:
            menor_peso = peso

# Exibe os resultados finais
print(f"\nO maior peso digitado foi: {maior_peso} kg")
print(f"O menor peso digitado foi: {menor_peso} kg")

