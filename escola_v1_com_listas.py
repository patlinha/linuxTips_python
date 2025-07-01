#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das atividades
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana","Carlos","Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica),
    ("Dança", aula_danca)
]


# Listar alunos em cada atividade por sala

for nome_atividade, lista_aluno in atividades:
    atividade_sala1 = []
    atividade_sala2 = []

    for nome_aluno in lista_aluno:
        
        if nome_aluno in sala1:
            atividade_sala1.append(nome_aluno)
        elif nome_aluno in sala2:
            atividade_sala2.append(nome_aluno)

    print("{:-^40}".format(f"Alunes da atividade {nome_atividade}"))
    print("{:40}".format(f"Sala 1: {atividade_sala1}"))
    print("{:40}".format(f"Sala 2: {atividade_sala2}"))
print("-" * 40)
