# De qual estado é o seu time? Escolha um time!

time = str(input("Digite o nome do seu time de futebol: "))

if ("Flamengo", "Fluminense", "Vasco", "Botafogo"):
    print("É um time Carioca!")
    
elif ("Corinthians", "Palmeiras", "Santos",) or ("São Paulo"):
    print("É um time Paulista!")
    
elif ("Internacional") or ("Grêmio") or ("Bagé") or ("Caxias"):
    print("É um time Gaúcho!")
else:
    print("É um time de outro Estado!")
