# Crie um algoritmo que receba dois números e mostre a diferença somente quando
# o primeiro for maior que o segundo.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

if numero_1 > numero_2:
    diferenca = numero_1 - numero_2
    print(f"O resultado da subtração é: {diferenca:.2f}")
else:
    print(f"O primeiro número é menor que o segundo número!")

