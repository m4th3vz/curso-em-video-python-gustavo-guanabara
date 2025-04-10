'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

prim = int(input("Primeiro termo: "))
raz = int(input("Razão da PA: "))

termo = prim
total = 0
mais = 10

while mais != 0:
    count = 0
    while count < mais:
        print(termo, end=' → ')
        termo += raz
        count += 1
        total += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais? (0 para sair) "))

print(f"Progressão finalizada com {total} termos mostrados.")

