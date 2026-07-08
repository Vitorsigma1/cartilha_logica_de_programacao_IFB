# Escreva um algoritmo que leia dois números, calcule o produto entre eles,
# mostre o resultado e os números recebidos.

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

resultado = primeiro_numero * segundo_numero

print(f"O resultado da multiplicação é: {resultado:.2f}")
print(f"Os números usados na multiplicação são: {primeiro_numero:.2f} e {segundo_numero:.2f}")
