# Ler a idade de uma pessoa expressa em anos, meses e dias e mostre a idade
# dessa pessoa expressa apenas em dias.
while True:
    anos = int(input("Digite a idade de uma pessoa em anos: "))
    if anos > 100:
        print("[ERROR!] Idade da pessoa em Anos Incorreta!\n")
    else:
        print("Idade aceita com sucesso!\n")
        break
              
while True:
    meses = int(input("Além dos anos, quantos meses de idade tem essa pessoa: "))
    if meses > 12:
        print("[ERROR!] Idade da pessoa em Meses Incorreta!\n")
    else:
        print("Idade aceita com sucesso!\n")
        break

while True:
    dias = int(input("Além dos anos e meses, quantos dias de idade tem essa pessoa: "))
    if dias > 31:
        print("[ERROR!] Idade da pessoa em Dias Incorreta!\n")
    else:
        print("Idade aceita com sucesso!\n")
        break

anos_em_dias = anos * 365
meses_em_dias = meses * 30
idade_em_dias = anos_em_dias + meses_em_dias + dias

print("A idade da pessoa é:", idade_em_dias, "dias")
