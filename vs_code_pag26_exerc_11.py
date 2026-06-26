# Obter a média aritmética das quatro notas.
primeira_nota = float(input("Digite a primeira nota de 0 à 10: "))
segunda_nota = float(input("Digite a segunda nota de 0 à 10: "))
terceira_nota = float(input("Digite a terceira nota de 0 à 10: "))
quarta_nota = float(input("digite a quarta nota de 0 à 10: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print("A média aritmética das quatro notas é: {:.2f}".format(media))
