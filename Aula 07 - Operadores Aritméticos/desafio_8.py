# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input("Digite um valor em metros: \n"))
# print("{} metro(s), convertido(s) em centímetros, é {}cm; convertido(s) em milímetros é {}mm.".format(n, (n*100), (n*1000)))

print(f"{n} metros são {n * 1000} kilômetros.")
print(f"{n} metros são {n * 100} hectômetros.")
print(f"{n} metros são {n * 10} decâmetros.")

print(f"{n} metros são {n * 1} metros.")

print(f"{n} metros são {n / 10} decímetros.")
print(f"{n} metros são {n / 100} centímetros.")
print(f"{n} metros são {n / 1000} milímetros.")
