# O custo ao consumidor de um carro novo é a soma do Custo de Fábrica com a
# Percentagem do Distribuidor e dos Impostos. (Aplicados ao Custo de Fábrica!)
# Supondo que a Percentagem do Distribuidor seja de 28% e os Impostos de 45%.
# Escreva um algoritmo para ler o Custo de Fábrica de um carro e escrever ao
# consumidor.

custo_fabrica = float(input("Digite o Custo de Fábrica de um carro: R$"))

percentagem_distribuidor = custo_fabrica * (28 / 100)
impostos_sobre_veiculos = custo_fabrica * (45 / 100)

custo_consumidor = custo_fabrica + percentagem_distribuidor + impostos_sobre_veiculos

print(f"O Valor Final do Carro para o consumidor é: {custo_consumidor:.2f}")

