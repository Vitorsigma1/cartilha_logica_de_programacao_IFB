# Uma empresa de energia elétrica calcula o consumo em kw/h. Faça um algoritmo que receba o número da 
# conta, aleitura anterior e a leitura atual, calcule o valor a ser pago, sabendo que a tarifa do kw/h é 
# de 0.20725. Mostre o número da conta e o consumo mensa de energia do um usuário e o valor da conta a 
# pagar.

print("**********************************************************************")
print("**********|COMPANHIA DE ELETRICIDADE DO ESTADO DE SÃO PAULO|**********")
print("**********************************************************************\n")

numero_conta = float(input("Digite o número da sua conta: "))
leitura_anterior = float(input("Digite o número da leitura anterior: "))
leitura_atual = float(input("Digite o número da leitura atual: "))

tarifa = 0.20725
consumo_mensal = leitura_atual - leitura_anterior
valor_da_conta = consumo_mensal * tarifa

print("O número da sua conta é: ", "{:.0f}".format(numero_conta))
print("O consumo mensal do usuário é:", "{:.2f}".format(consumo_mensal), "kw/h")
print("O valor da conta de energia é: R$","{:.2f}".format(valor_da_conta))
