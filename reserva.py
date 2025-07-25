#!/usr/bin/env python3

'''
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis 
para alugar e o preço de cada quarto, esta informação está disponível em um arquivo de texto
separado por vírgulas `quartos.txt`

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar a escolha em outro arquivo contendo as reservas `reservas.txt`
# cliente, quarto, dias
Bruno, 3, 12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma msg 
informando que já está reservado
'''

import os
import sys
import logging
from datetime import datetime

path = os.curdir
filepathQuartos = os.path.join(path, "quartos.txt")
filepathReservas = os.path.join(path, "reservas.txt")
timestamp = datetime.now().isoformat()
valorReserva = 0

try:
    for linha in open(filepathQuartos):
        codigo, nomeQuarto, precoDiaria = linha.split(",")
        print(f"{codigo}   {nomeQuarto}   {precoDiaria}")
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)

nomeClienteParaReserva = input("Informe o nome do cliente: ")
numeroQuartoParaReserva = int(input("Informe o código do quarto: "))
numeroDiasParaReserva = int(input("Informe a quantidade de dias: "))

try:
    for linha in open(filepathReservas):
        cliente, quarto, dias = linha.split("#")
        print(f"{cliente}   {quarto}   {dias}")
        quarto = quarto.strip()
        quarto = int(quarto)
        if numeroQuartoParaReserva == quarto:
            print(f'Este quarto já está reservado')
            sys.exit(1)        
            

except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
except ValueError as e:
    print(f"{str(e)}")
    sys.exit(1)  

try:
    for linha in open(filepathQuartos):
        codigo, nomeQuarto, precoDiaria = linha.split(",")
        print(f"{codigo}   {nomeQuarto}   {precoDiaria}")
        if codigo != "# codigo":
            codigo = codigo.strip()
            codigo = int(codigo)
            if codigo == numeroQuartoParaReserva:
                precoDiaria = precoDiaria.strip()
                precoDiaria = float(precoDiaria)
                valorReserva = precoDiaria * numeroDiasParaReserva
    print(f'Total a pagar: {valorReserva}')
            

except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
except ValueError as e:
    print(f"{str(e)}")
    sys.exit(1)   

try:
    with open(filepathReservas, "a") as file_:
        file_.write(f"{nomeClienteParaReserva} --> quarto# {numeroQuartoParaReserva} # {numeroDiasParaReserva} dias ({timestamp})\n")
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
except ValueError as e:
    print(f"{str(e)}")
    sys.exit(1)   