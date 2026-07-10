# Faça um algoritmo que leia uma temperatura fornecida em graus fahrenheit e converta para seu equivalente
# em graus centígrados.

graus_fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))

graus_centigrados = 5/9 * (graus_fahrenheit - 32)

print("A temperatura em graus fahrenheit é:", "{:.2f}".format(graus_fahrenheit), "e a temperatura em graus centígrados é:", "{:.2f}".format(graus_centigrados))