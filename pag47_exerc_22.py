# Faça um Programa para calcular e imprimir o salário bruto a ser recebido por
# um funcionário em um mês, o algoritmo deverá utilizar os seguintes dados:
# número de horas que o funcionário trabalhou no mês, valor recebido por hora de
# trabalho e número de filhos com idade menor do que 14 anos (para adicionar o
# salário família). Considerar o valor do salário família por filho.

numero_de_horas = float(input("Digite o número de horas trabalhadas num mês: "))
horas_trabalhadas = float(input("Digite o valor da hora de  trabalho: R$ "))
numero_de_filhos = int(input("Digite o número de filhos menores de 14 anos: "))

salario_bruto = numero_de_horas * horas_trabalhadas * numero_de_filhos

print(f"O salário bruto do funcionário é: R${salario_bruto:.2f}")
print(f"O número de horas trabalhadas do funcionário é: {numero_de_horas:.2f}")
print(f"O número de filhos menores de 14 anos: {numero_de_filhos:.0f}")

