#!/user/bin/env python

"""Imprime a msg de um email

"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
   print("Informe o nome do arquivo dos emails")
   sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path,filename) # emails.txt
templatepath = os.path.join(path,templatename) # email_tmpl.txt

clientes = []
for line in open(filepath):
   name, email = (line.split(","))

   #TODO: substituir por envio de email
   print(f"Enviando email para: {email}")
   print()
   print(
      open(templatepath).read()
      % {
      "nome": name,
      "produto":"caneta",
      "texto": "lorem ipsum",
      "link": "https://canetasincriveis.com",
      "quantidade":1,
      "preco": 50.5
      })
   print("-" * 50)
