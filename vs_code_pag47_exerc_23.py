# Escreva um algoritmo que lê o código da peça 1, a quantidade de peças 1 e o valor unitário da peça 1 e 
# também leia o código da peça 2, a quantidade de peças 2 e o valor unitário da peça 2 e a percentagem de
# 'IPI' a ser acrescentado e calcule o valor total a ser pago.

codigo_peca_1 = int(input("Digite o código da peça 1: "))
quantidade_peca_1 = int(input("Digite a quantidade de peças 1: "))
valor_peca_1 = float(input("Digite o valor unitário da peça 1: R$"))

codigo_peca_2 = int(input("Digite o código da peça 2: "))
quantidade_peca_2 = int(input("Digite a quantidade de peças 2: "))
valor_peca_2 = float(input("Digite o valor unitário da peça 2: R$"))

preco_peca_1 = quantidade_peca_1 * valor_peca_1
preco_peca_2 = quantidade_peca_2 * valor_peca_2
taxa_de_ipi = (preco_peca_1 + preco_peca_2) * (3 / 100)

total_a_pagar = preco_peca_1 + preco_peca_2 + taxa_de_ipi

print("O valor a ser pago pelas peças é: R$", "{:.2f}".format(total_a_pagar))
