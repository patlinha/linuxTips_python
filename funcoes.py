"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility --> uma função resolve apenas um problema

def f(x): #assinatura
     result = 5 * (x / 2)
     return result

def double(x):
     return x*2

valor = double(f(10))

print(valor)
print(valor == 50)

###
#funções sem retorno explícito são procedures
#(retorna 'None' implicitamente, pq toda função em python retorna algo)

def print_in_upper(texto):
     print(texto.upper())

print_in_upper("pati")

###

from math import sqrt

def heron(a, b, c):
     """Calcula a área de um triângulo"""
     perimeter = a + b + c
     s = perimeter / 2
     #sqrt = num ** 0.5
     area = sqrt(s * (s-a) * (s-b) * (s-c))
     return area

def heron2(params):
     return heron(*params)

triangulos = [
     (3, 4, 5),
     (5, 12, 13),
     (8, 15, 17),
     (12, 35, 37),
     (3, 4, 5)
]

"""
print(list(map(heron2, triangulos)))
"""

for t in triangulos:
     area = heron(t[0], t[1], t[2])
     print(f"A área do triângulo é: {area}")

