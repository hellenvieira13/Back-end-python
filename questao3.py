frase = input("Digite uma frase: ")

palavras = frase.lower().split()  
frequencia = {}  

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1


for palavra, quantidade in frequencia.items():
    print(f"{palavra}: {quantidade}")
