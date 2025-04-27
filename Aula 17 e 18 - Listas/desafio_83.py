'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input("Digite uma expressão: ")
pilha = []

for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if pilha:
            pilha.pop()
        else:
            # Fechou parêntese sem abrir
            print("Inválido")
            break
else:
    # Só executa se o `for` terminar normalmente (sem break)
    if not pilha:
        print("Válido")
    else:
        print("Inválido")
