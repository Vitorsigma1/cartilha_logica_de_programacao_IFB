# Obter a média aritmética das quatro notas. Se a média for maior ou igual a
# sete, o aluno está aprovado. Caso contrário o aluno está reprovado.

primeira_nota = float(input("Digite a primeira nota do aluno de 0 à 10: "))
segunda_nota = float(input("Digite a segunda nota do aluno de 0 à 10: "))
terceira_nota = float(input("Digite a terceira nota do aluno de 0 à 10: "))
quarta_nota = float(input("Digite a quarta nota do aluno de 0 à 10: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

if media >= 7:
    print("O aluno está Aprovado! Parabéns!")

else:
    print("O aluno foi reprovado! Sinto muito!")
