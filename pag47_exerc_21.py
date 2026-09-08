# Dado o preço de um produto em reais, converta esse valor para o equivalente em
# dólares. O programa deverá ler o preço e a taxa de conversão para o dólar.

preco_produto = float(input("Digite o valor do Produto em Reais: "))
valor_atual_dolar = float(input("Digite o valor atual do dólar: "))

conversao = preco_produto * valor_atual_dolar

print(f"O valor atual do dolar é: {valor_atual_dolar:.2f}")
print(f"O preço do produto em dólares é: {conversao: .2f}")
