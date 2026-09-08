# Em uma empresa, será solicitado o salário de um determinado funcionário para
# se calcular seu novo salário, sendo que, se este  tiver um salário inferior a
# R$1000.00, o reajuste será de 8%.

salario_atual = float(input("Digite o Salário Atual do Funcionário: R$"))

if salario_atual < 1000:
    novo_salario = salario_atual * 1.08
    print(f"O Novo Salário do Funcionário é: R${novo_salario:.2f}")
else:
    print("O Salário do funcionário e maior que R$1000,00!")
          



