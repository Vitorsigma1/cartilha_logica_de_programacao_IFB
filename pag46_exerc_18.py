# Uma empresa de energia elétrica calcula o valor da conta de luz de acordo com
# o consumo em kw/h . Faça um algoritmo que receba o número da conta, a leitura
# anterior, a leitura atual. Calcule o valor a ser pago, sabendo que a tarifa do
# kw/h é de 0.20725. Mostre o número da conta e o consumo de luz de um usuário e
# o quanto o usuário irá pagar.
print("********************************************************************")
print("**********COMPANHIA DE ELETRICIDADE DO ESTADO DE SÃO PAULO**********")
print("********************************************************************\n")

numero_da_conta = float(input("Digite o Número da sua Conta de Energia Elétrica: "))
numero_da_leitura_anterior = int(input("Digite o Número da Leitura Anterior: "))
numero_da_leitura_atual = int(input("Digite o Número da Leitura Atual: "))
tarifa = 0.20275

consumo_mensal = numero_da_leitura_atual - numero_da_leitura_anterior
valor_da_conta = consumo_mensal * tarifa

print(f"O número da conta é: {numero_da_conta}")
print(f"O consumo mensal de energia do usuário é: {consumo_mensal:.2f}kw/h")
print(f"O valor da conta à pagar é: R${valor_da_conta:.2f}")

