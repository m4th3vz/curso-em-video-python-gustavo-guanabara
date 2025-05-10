"""
Faça um minissistema que utilize o interactive help do Python

O usuário vai digitar o comando e o manual vai aparecer.

Quando o usuário digitar a palavra "FIM", o programa se encerrará!.

OBS: use cores.
"""

import colorama
from colorama import Fore

# Inicializa o colorama
colorama.init(autoreset=True)

def exibir_manual():
    print(Fore.CYAN + "Digite o comando que deseja ver o manual ou 'FIM' para encerrar:")

    while True:
        comando = input(Fore.YELLOW + "> ").strip()
        
        if comando.upper() == "FIM":
            print(Fore.RED + "Encerrando o programa. Até logo!")
            break
        
        try:
            # Exibe o manual do comando
            print(Fore.GREEN + f"\nManual do comando '{comando}':\n")
            help(comando)
        except Exception as e:
            print(Fore.RED + f"\nErro: {e}. Comando não encontrado ou inválido!\n")

# Chamando a função para exibir o manual
exibir_manual()
