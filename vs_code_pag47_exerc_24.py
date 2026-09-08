# Escreva um algoritmo que lê o número de um vendedor, o seu salário fixo, o total de vendas por ele 
# efetuadas e o percentual que ganha sobre o total de vendas. Calcule o salário total do vendedor. Escreva
# o número do vendedor e o salário total.

numero_do_vendedor = int(input("Digite o Número do Vendedor: "))
salario_fixo = float(input("Digite o Salário Fixo do Vendedor: R$"))
valor_total_de_vendas = float(input("Digite o Valor Total de Vendas: R$"))
porcentual_vendas = float(input("Digite o porcentual sobre as Vendas: %"))

total_porcentual = valor_total_de_vendas * (porcentual_vendas / 100)

salario_total = salario_fixo + valor_total_de_vendas + total_porcentual

print("O Número do Vendedor é: ", "{:.0f}".format(numero_do_vendedor))
print("O Salário do Vendedor é: ", "{:.2f}".format(salario_total))
