# Faça um algoritmo que receba um número e mostre a sua quinta parte somente
# quando ela for menor que cinquenta ou maior que mil.

numero = int(input("Digite um numero: "))

if numero < 50 or numero > 1000:
    dividido = numero / 5
    print(f"A quinta parte do número é: {dividido:.2f}")

