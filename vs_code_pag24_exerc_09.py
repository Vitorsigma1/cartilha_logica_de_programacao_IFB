# Ler 5 valores, calcular e mostrar a média aritmética destes valores. Se o resultado for maior que 100, 
# mostrar a palavra "MAIOR", senão mostrar a palavra "MENOR".

primeiro_valor = float(input("Digite um número: "))
segundo_valor = float(input("Digite outro número: "))
terceiro_valor = float(input("Digite mais um número: "))
quarto_valor = float(input("Digite novamente um número: "))
quinto_valor = float(input("Digite mais esta vez um número: "))

media = (primeiro_valor + segundo_valor + terceiro_valor + quarto_valor + quinto_valor) / 5
print("A média dos números são:", media)

if media > 100:
    print("MAIOR")
else:
    print("MENOR")
