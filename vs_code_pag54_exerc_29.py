# Escreva um algoritmo que receba um número e mostre a sua metade somente quando ela for maior que 
# cinquenta.

numero = int(input("Digite um número: "))

metade = numero / 2

if metade > 50:
    print("A metade de " "{:.0f}" " é " "{:.0f}"", que é maior que cinquenta." .format(numero, metade))
else:
    print("A metade do número digitado é menor que cinquenta!")