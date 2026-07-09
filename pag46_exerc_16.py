# Leia dois valores para as variáveis "A" e "B", efetue a troca dos valores de
# forma que a variável "A" passe a ter o valor da variável "B" e que a variável
# "B", tenha o valor da variável "A". Apresente os valores trocados.

valor_de_a = input("Digite o valor de 'A': ")
valor_de_b = input("Digite o valor de 'B': ")

print("O valor de 'A' é:", valor_de_a, "e o valor de 'B' é:", valor_de_b)

valor_de_a, valor_de_b = valor_de_b, valor_de_a

print("O valor de 'A' trocado é:", valor_de_a, "e o valor de 'B' trocado é:", valor_de_b)





