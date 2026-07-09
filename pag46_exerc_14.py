# Crie um algoritmo que receba a idade de três pessoas, calcule e mostre a
# média da idades.


while True:
    primeira_pessoa = int(input("Digite a idade da primeira pessoa: "))
    if primeira_pessoa <= 0:
        print("[ERROR] Digite a idade correta!\n")
    else:
        print("Valor da Idade aceito!\n")
        break
    
while True:
    segunda_pessoa = int(input("Digite a idade da segunda pessoa: "))
    if segunda_pessoa <= 0:
        print("[ERROR] Digite a idade correta!\n")
    else:
        print("Valor da Idade aceito!\n")
        break
    
while True:    
    terceira_pessoa = int(input("Digite a idade da terceira pessoa: "))
    if terceira_pessoa <= 0:
        print("[ERROR] Digite a idade correta!\n")
    else:
        print("Valor da Idade aceito!\n")
        break

media_idades = (primeira_pessoa + segunda_pessoa + terceira_pessoa) / 3

print(f"A média da idade das três pessoas é: {media_idades:.2f}")
