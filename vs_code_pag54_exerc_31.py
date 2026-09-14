# Faça um algoritmo que receba um número e mostre a sua quinta parte somente quando ela for menor que 
# cinquenta ou maior que mil.

numero = int(input("Digite um número: "))
quinta_parte = numero / 5

if quinta_parte < 50 or quinta_parte > 1000:
    print("A quinta parte de " "{:.0f}" " é " "{:.1f}"", que é menor que cinquenta e maior que mil.".format(numero, quinta_parte))
else:
    print("A quinta parte do número digitado não é menor que cinquenta e nem maior que mil!")
    