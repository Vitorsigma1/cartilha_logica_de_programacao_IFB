# Leia dois valores para as variáveis 'A' e 'B', efetue a troca dos valores de forma que a variável 'A' 
# passe a ter o valor da variável 'B', e que a variável 'B', tenha o valor da variável 'A'. 
# Apresentar os valores trocados.

valor_da_variavel_a = input("Digite o valor da variável 'A': ")
valor_da_variavel_b = input("Digite o valor da variável 'B': ")

print("O valor da variável 'A' é:", valor_da_variavel_a, " e o valor da variável 'B' é:", valor_da_variavel_b)

valor_da_variavel_a, valor_da_variavel_b = valor_da_variavel_b, valor_da_variavel_a

print("O valor da variável 'A' trocado é:", valor_da_variavel_a, "e o valor da variável 'B' trocado é:", valor_da_variavel_b)

