
# Escreva um algoritmo que lê um número de um vendedor, o seu salário fixo, o
# total de vendas por ele efetuadas e o percentual que ganha sobre o total de
# vendas. Calcule o salário total do vendedor. Escreva o número do vendedor e o
# salário total.

numero_vendedor = int(input("Digite o Número do Vendedor: "))
salario_fixo = float(input("Digite o Salário Fixo do Vendedor: R$"))
valor_total_de_vendas = float(input("Digite o Valor do Número de Vendas: R$"))
porcentual_de_vendas = float(input("Digite o Porcentual de Vendas: %"))

total_percentual = valor_total_de_vendas * (porcentual_de_vendas / 100)

salario_total = salario_fixo + valor_total_de_vendas + total_percentual

print(f"O Número do Vendedor é: {numero_vendedor:.0f}")
print(f"O Salário Total do Vendedor: R${salario_total:.2f}")

