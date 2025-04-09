''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

num = int(input("Descubra se um número é primo: \n"))

if num < 2:
    print(f"O número {num} não é primo.")
else:
    isPrime = True
    for i in range(2, int(num ** 0.5) + 1):  # Itera até a raiz quadrada de num
        if num % i == 0:
            isPrime = False
            break  # Sai do loop assim que encontrar um divisor
    
    print(f"O número {num} é primo." if isPrime else f"O número {num} não é primo.")
