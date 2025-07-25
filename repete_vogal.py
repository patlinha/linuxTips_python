palavras = []

while True:
    palavra = input("Digite uma palavra (ou aperte enter para sair): ").strip()
    palavra_final = ""
    if not palavra:
        break
    else:
        for letra in palavra:
            # TODO: Remover acentuação usando função
            if letra.lower() in "aeiou":
                palavra_final += letra * 2
            else:
                palavra_final += letra
        #if ternário
        #palavra_final += letra * 2 if letra.lower() in "aeiou" else letra
        palavras.append(palavra_final)
print(*palavras, sep='\n')
