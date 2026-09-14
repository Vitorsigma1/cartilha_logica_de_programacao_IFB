# Elabore um algoritmo que receba um número e mostre o número e o sêxtuplo somente quando o número for 
# maior que noventa.

numero = int(input("Digite um número: "))
sextuplo = numero * 6

if numero >= 90:
    print("O número digitado foi: " "{:.0f}" ", o seu sêxtuplo é: " "{:.0f}".format(numero, sextuplo))
else:
    print("O número digitado é menor que noventa!")
    