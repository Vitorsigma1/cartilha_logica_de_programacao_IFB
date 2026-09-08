# O custo ao consumidor de um carro novo, é a soma do Custo de Fábrica com a Percentagem do Distribuidor e
# dos Impostos.(Aplicados ao Custo de Fábrica). Supondo que a Percentagem do Distribuidor seja de 28% e os
# Impostos de 45%. Escreva um algoritmo para ler o Custo de Fábrica de um carro e escrever ao consumidor.

custo_de_fabrica = float(input("Digite o Custo de Fábrica do Automóvel: R$"))

percentagem_distribuidor = custo_de_fabrica * (28 / 100)
imposto_veiculo = custo_de_fabrica * (45 / 100)

custo_total_veiculo = custo_de_fabrica + percentagem_distribuidor + imposto_veiculo

print("O valor do veículo para Consumidor Final é: R$", "{:.2f}".format(custo_total_veiculo))
