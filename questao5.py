frase = input("Digite a frase: ")

stopwords = {"de", "da", "do", "das", "dos", "e"}
palavras = frase.lower().split()

acronimo = "".join([p[0].upper() for p in palavras if p not in stopwords])

print("Acrônimo:", acronimo)
