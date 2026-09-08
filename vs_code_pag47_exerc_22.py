# Faça um programa para calcular e imprimir o salário bruto a ser recebido por um funcionário em um mês. 
# O algoritmo deverá utilizar os seguintes dados: número de horas que o funcionário trabalhou no mês, valor
# recebido por hora de trabalho e número de filhos com idade menor do que 14 anos (Para adionar o salário 
# família). Considerar o valor do salário família por filho.

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora_trabalho = float(input("Digite o valor da hora de trabalho: R$"))
numero_de_filhos = int(input("Digite o número de filhos menores de 14 anos: "))

salario_bruto = horas_trabalhadas * valor_hora_trabalho * numero_de_filhos

print("O valor do salário bruto é: R$", "{:.2f}".format(salario_bruto))
print("O valor da hora de trabalho é: R$", "{:.2f}".format(valor_hora_trabalho))
print("O número de filhos menores de 14 anos é:", "{:.0f}".format(numero_de_filhos))

