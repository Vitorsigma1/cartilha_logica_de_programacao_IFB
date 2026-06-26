# Obter a média aritmética das quatro notas.

primeira_nota = float(input("Digite a primeira nota do aluno de 0 à 10: "))
segunda_nota = float(input("Digite a segunda nota do aluno de 0 à 10: "))
terceira_nota = float(input("Digite a terceira nota do aluno de 0 à 10: "))
quarta_nota = float(input("Digite a quarta nota do aluno de 0 à 10: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"A média das quatro notas é: {media:.2f}")
