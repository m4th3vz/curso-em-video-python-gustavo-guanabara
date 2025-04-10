''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

menu = """
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
Escolha uma opção: """

a = int(input("Número 1: "))
b = int(input("Número 2: "))

while True:
    opcao = input(menu)

    if opcao == "1":
        resultado = a + b
        print(f"A soma de {a} com {b} é {resultado}\n")

    elif opcao == "2":
        resultado = a * b
        print(f"A multiplicação de {a} com {b} é {resultado}\n")

    elif opcao == "3":
        if a > b:
            print(f"O número {a} é maior que o número {b}\n")
        elif b > a:
            print(f"O número {b} é maior que o número {a}\n")
        else:
            print("Os dois números são iguais.\n")

    elif opcao == "4":
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))

    elif opcao == "5":
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")
