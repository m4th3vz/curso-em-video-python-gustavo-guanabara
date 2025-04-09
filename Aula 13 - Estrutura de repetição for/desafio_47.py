# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

for i in range(0, 51, 2):
    print(i)

# Segunda forma de fazer o mesmo exercício
for num in range(1, 51):
    if num % 2 == 0:
        print(num)
