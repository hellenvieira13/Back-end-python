frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0

for char in frase.lower():
    if char.isalpha():  # verifica se é letra
        if char in "aeiou":
            vogais += 1
        else:
            consoantes += 1

print(f"Vogais: {vogais} | Consoantes: {consoantes}")
