#! /usr/bin/env python3

"""Hello World Multi Linguas
Dependendo da língua configurada no ambiente o programa exibe a msg de acordo com ela

Como usar:
Tenha a variável LANG devidamente configurada ex.:
    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "patlinha"
__license__ = "Unlicense"


#current_language = "en_US"
import os
import sys

print(f"{sys.argv}")
arguments = {
    "lang" : None,
    "count" : 1
}
for arg in sys.argv[1:]:
    #TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US" : "Hello, World!\t",
    "pt_BR" : "Olá, Mundo!\t",
    "it_IT" : "Ciao, Mondo!\t",
    "es_SP" : "Hola, Mundo!\t",
    "fr_FR" : "Bonjour, Monde!\t"
}

print(msg[current_language] * int(arguments["count"]))
