
# De qual estado é o seu time? escolha um time!

time = str(input("Digite o nome do seu Time de Futebol: "))

if time in ["Flamengo", "Fluminense", "Vasco", "Botafogo"]:
    print("É um Time Carioca!")

elif time in ["Corinthians", "Santos", "Palmeiras", "São Paulo"]:
    print("É um Time Paulista!")

elif time in ["Internacional", "Grêmio", "Bagé", "Caxias"]:
    print("É um Time Gaúcho!")

else:
    print("É um Time de outro Estado!")
    
