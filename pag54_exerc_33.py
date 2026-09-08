# Elabore um algoritmo que receba um número e mostre o número e o sêxtuplo
# somente quando o número for maior que noventa.

numero = int(input("Digite um número: "))

if numero > 90:
    sextuplo = numero * 6
    print(f"O número digitado é: {numero:.2f} ")
    print(f"O sextuplo desse numero é: {sextuplo:.2f} ")
else:
    print(f"O número digitado é menor que noventa!")
