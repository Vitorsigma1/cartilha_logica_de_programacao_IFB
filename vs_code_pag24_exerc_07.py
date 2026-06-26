# Ler a idade de uma pessoa expressa em anos, meses e dias e mostrar a idade dessa pessoa expressa apenas
# em dias.
while True:
    idade_em_anos = int(input("Digite a idade da pessoa em anos: "))
    if idade_em_anos > 100:
        print("[ERROR!] A idade da pessoa em anos está Incorreta\n")
    else:
        print("Idade da pessoa em anos aceita com Sucesso!\n")
        break

while True:
    idade_em_meses = int(input("Digite a idade da pessoa em meses: "))
    if idade_em_meses > 12:
        print("[ERROR!] A idadde da pessoa em meses está Incorreta!\n")
    else:
        print("Idade da pessoa em meses aceita com Sucesso!\n")
        break

while True:
    idade_em_dias = int(input("Digite a idade da pessoa em dias: "))
    if idade_em_dias > 30:
        print("[ERROR!] A idade da pessoa em dias está Incorreta!\n")
    else:
        print("Idade da pessoa em dias aceita com Sucesso!\n")
        break

anos_em_dias = idade_em_anos * 365
meses_em_dias = idade_em_meses * 30
idade_total_em_dias = anos_em_dias + meses_em_dias + idade_em_dias
print("A idade da pessoa é", idade_total_em_dias, "dias")
