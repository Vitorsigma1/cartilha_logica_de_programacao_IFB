# Faça um algoritmo que receba a matrícula e as três notas do aluno, calcule a
# sua média, sabendo que a primeira nota tem peso dois, a segunda nota tem
# peso três e a terceira nota tem peso quatro. Mostre a matrícula e a média do
# aluno.

numero_da_matricula = float(input("Digite o Número da Matrícula do Aluno: "))
primeira_nota = float(input("Digite a Primeira Nota do Aluno de 0 a 10: "))
segunda_nota = float(input("Digite a Segunda Nota do Aluno de 0 a 10: "))
terceira_nota = float(input("Digite a Terceira Nota do Aluno de 0 a 10: "))

primeira_nota = primeira_nota * 2
segunda_nota = segunda_nota * 3
terceira_nota = terceira_nota * 4

soma_pesos = 2 + 3 + 4

media = (primeira_nota + segunda_nota + terceira_nota) / soma_pesos

print(f"O Número da Matrícula do Aluno é: {numero_da_matricula:.0f}")
print(f"A Média das Notas é: {media:.2f}")
