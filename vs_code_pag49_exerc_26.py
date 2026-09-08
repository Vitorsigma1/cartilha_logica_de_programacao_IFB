# Em uma empresa, será solicitado o Salário de um determinado funcionário para se calcular seu novo 
# salário, sendo que, se este tiver um salário inferior a R$1000,00, o reajuste será de 8%.

salario_atual = float(input("Digite o Salário Atual do Funcionário: R$"))

if salario_atual < 1000:
    novo_salario = salario_atual * 1.08
    print("O Novo Salário do Funcionário é: R$", "{:.2f}".format(novo_salario))
else:
    print("O Salário do Funcionário já é maior que R$1000,00!")
