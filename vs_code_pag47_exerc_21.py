# Dado o preço de um produto em reais, converta esse valor para o equivalente em dólares. O programa 
# deverá ler o preço e a taxa de conversão para o dólar.

valor_produto = float(input("Digite o valor do produto em Reais: "))
valor_atual_dolar = float(input("Digite o Valor Atual do Dólar: "))

conversao = valor_produto * valor_atual_dolar

print("O valor do Atual do Dólar é:", "{:.2f}".format(valor_atual_dolar))
print("O valor do Produto em Dólares é:", "{:.2f}".format(conversao))
