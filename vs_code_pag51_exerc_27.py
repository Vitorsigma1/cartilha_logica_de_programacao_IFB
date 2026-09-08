# Em uma Empresa, será solicitado o salário de um determinado funcionário para se calcular seu novo 
# salário, sendo que, se tiver um salário inferior a R$1000,00, o reajuste será de 8%, caso contrário o 
# reajuste será de 5%.

salario_atual = float(input("Digite o Salário Atual do Funcionário: R$"))

if salario_atual < 1000:
    novo_salario = salario_atual * 1.08
    print("O Novo Salário do Funcionário é: R$", "{:.2f}".format(novo_salario))
else:
    novo_salario = salario_atual * 1.05
    print("O Novo Salário do Funcionário é: R$", "{:.2f}".format(novo_salario))
