palavras = input("Digite palavras separadas por espaço: ").split()

conta_a = 0
conta_palin = 0
conta_longa = 0
conta_comum = 0

for palavra in palavras:
    categorias = []
    if palavra.lower().startswith('a'):
        categorias.append("Começa com A")
        conta_a += 1
    if palavra.lower() == palavra[::-1].lower():
        categorias.append("É palíndromo")
        conta_palin += 1
    if len(palavra) > 7:
        categorias.append("Palavra longa")
        conta_longa += 1
    if not categorias:
        categorias.append("Palavra comum")
        conta_comum += 1
    print(f"{palavra} → {', '.join(categorias)}")

print("\nResumo:")
print(f"Palavras que começam com A: {conta_a}")
print(f"Palíndromos: {conta_palin}")
print(f"Palavras longas: {conta_longa}")
print(f"Palavras comuns: {conta_comum}")
