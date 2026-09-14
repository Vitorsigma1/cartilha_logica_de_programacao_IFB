# Construa um algoritmo que receba um número e mostre o seu sêxtuplo somente quando o resultado for menor
# que trezentos.

numero = int(input("Digite um número: "))
sextuplo = numero * 6

if sextuplo <= 300:
    print("O número digitado foi: " "{:.0f}"", o seu sêxtuplo é: " "{:.0f}".format(numero, sextuplo))
else:
    print("O sêxtuplo do número digitado é maior que trezentos!")
