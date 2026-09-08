# Faça um algoritmo que receba um número e mostre o número somente quando o
# número for par.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número que você digitou, {numero:.2f} é par!")
else:
    print(f"O número que você digitou não é par!")
