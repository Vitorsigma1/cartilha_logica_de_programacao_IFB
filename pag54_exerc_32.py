# Construa um algoritmo que receba um número e mostre o seu sêxtuplo somente
# quando o resultado não for menor que trezentos.

numero = int(input("Digite um número: "))

if numero < 300:
    sextuplo = numero * 6
    print(f"O número é: {numero:.2f} e o sêxtuplo é: {sextuplo:.2f}")
else:
    print(f"O número é: {numero:.2f} e é maior que trezentos!")

