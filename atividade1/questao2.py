
frase = input("Digite uma frase: ")

frase_limpa = frase.replace(" ", "").lower()

if frase_limpa == frase_limpa[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
