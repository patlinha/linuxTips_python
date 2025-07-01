#! /usr/bin/env python3

"""Hello World Multi Linguas
Dependendo da língua configurada no ambiente o programa exibe a msg de acordo com ela

Como usar:
Tenha a variável LANG devidamente configurada ex.:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "patlinha"
__license__ = "Unlicense"

if __name__ == "__main__":
    print("#####")
    print("Hello, World!")

print('patricia'.upper())



#current_language = "en_US"
import os

# Com um valor default em caso da variável não existir
current_language = os.getenv("LANG", "en_US")[:5]
#current_language = "fr_FR"
#current_language = "it_IT"

###########################################
# #comentário
# msg = "Hello, World!"
# #ordem de complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "fr_FR":
# 	msg = "Bonjour, Monde!"
#print(msg)
###########################################

# sets (Hash Table) - O(1) - constante
# dicts (Hash Table)
msg = {
    "en_US" : "Hello, World!",
    "pt_BR" : "Olá, Mundo!",
    "it_IT" : "Ciao, Mondo!",
    "es_SP" : "Hola, Mundo!",
    "fr_FR" : "Bonjour, Monde!"
}

print("#####")
print(msg[current_language])
print("#####")
