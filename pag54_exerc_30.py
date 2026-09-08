# Crie um algoritmo que receba um número e mostre o número e o seu dobro somente
# quando o número for maior que noventa e menor que cem.

numero = int(input("Digite um número: "))

if numero > 90 and numero < 100:
    dobro = numero * 2
    print(f"O número esta entre 90 e 100: {numero:.2f} e o dobro é: {dobro:.2f}")

else:
    print(f"O número não está entre 90 e 100!")
