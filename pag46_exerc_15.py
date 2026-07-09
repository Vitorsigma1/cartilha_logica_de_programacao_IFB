# Faça um algoritmo que receba dois números, calcule a divisão, a multiplicação
# , a soma, a diferença entre eles e mostre os resultados.

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

divisao_numeros = primeiro_numero / segundo_numero

multiplicacao_numeros = primeiro_numero * segundo_numero

soma_numeros = primeiro_numero + segundo_numero

subtracao_numeros = primeiro_numero - segundo_numero

print(f"O resultado da divisão dos dois números é: {divisao_numeros:.2f}")
print(f"O resultado da multiplicação dos dois números é: {multiplicacao_numeros:.2f}")
print(f"O resultado da soma dos dois números é: {soma_numeros:.2f}")
print(f"O resultado da subtração dos dois números é: {subtracao_numeros:.2f}")
