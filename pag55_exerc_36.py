# Escreva um algoritmo que receba um número e mostre o número, se ele estiver
# entre quinze (inclusive) e quarenta.

numero = int(input("Digite um número: "))

if numero >= 15 and numero <= 40:
    print(f"O número é {numero:.2f}, esta entre 15 e 40!")
else:
    print(f"O número que você digitou não está entre 15 e 40!")
