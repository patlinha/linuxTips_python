#!/usr/bin/env python3
"""Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`

"""

__version__ = "0.1.0"

import sys
import os
from datetime import datetime
import logging
import operator

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("pati", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

argumentos = sys.argv[1:]
operacoes_validas = {
    "sum" : lambda a, b: a + b,
    "sub" : operator.sub, 
    "mul" : lambda a, b: a * b,
    "div" : operator.truediv
}


while True:

    if not argumentos:
        operacao = input("operação: ")
        n1 = input("n1: ")
        n2 = input("n2: ")
        argumentos = [operacao, n1, n2]
    elif len(argumentos) != 3:
        print("Número de algumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operacao, *nums = argumentos

    if operacao not in operacoes_validas:
        print("Operação inválida")
        print(operacoes_validas)
        sys.exit(1)

    numeros_validados = []
    for num in nums:
        # TOD: Repetição while + exceptions
        if not num.replace(".","").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        numeros_validados.append(num)

    try:
        n1, n2 = numeros_validados
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    resultado = operacoes_validas[operacao](n1, n2)

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    print(f"O resultado é {resultado}")

    #print(f"{operacao}, {n1}, {n2} = {resultado}", file=open("prefixcalc.log", "a"))
    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} --> {operacao}, {n1}, {n2} = {resultado}\n")
    except PermissionError as e:
        log.error(str(e))
        sys.exit(1)

    argumentos = None

    if input("Pressione enter para continuar\ne qualquer tecla para sair\n"):
        break