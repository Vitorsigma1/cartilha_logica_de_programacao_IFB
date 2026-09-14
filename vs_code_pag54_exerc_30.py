# Crie um algoritmo que receba um número e mostre o número e o seu dobro somente quando o número for 
# maior que noventa e menor que cem.

numero = int(input("Digite um número: "))
dobro = numero * 2

if numero >= 90 and numero <= 100:
    print("O número digitado foi: ""{:.0f}" ", o seu dobro é: ""{:.0f}".format(numero, dobro))
else:
    print("O número digitado não está entre noventa e cem!")
    