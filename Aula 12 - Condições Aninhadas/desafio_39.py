'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
from datetime import datetime

nasc = int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year
# print("Ano atual: {}".format(ano_atual))
idade = (ano_atual - nasc)
if idade < 18:
    print(f"Você tem {idade} anos em {ano_atual} e vai se alistar daqui a {18 - idade} anos, em {nasc + 18}.")
elif idade > 18:
    print(f"Você tem {idade} anos e já passou seu período de alistamento.")
    print(f"Se não se alistou, deveria ter se alistado em {nasc + 18}, há {idade - 18} anos atrás.")
else:
    print(f"Você tem {idade} anos. Está na hora de se alistar.")
