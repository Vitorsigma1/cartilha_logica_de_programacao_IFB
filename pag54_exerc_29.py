# Escreva um algoritmo que receba um número e mostre a sua metade somente quando
# ela for maior que cinquenta.

numero = float(input("Digite um número: "))

if numero > 50:
    numero = numero / 2
    print(f"O número é maior que cinquenta! A metade é: {numero:.2f}")
else:
    numero = numero
    print(f"O número é menor que cinquenta! {numero:.2f}")
