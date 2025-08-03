"""\
Este módulo serve apenas de anotação
"""


# as funções são formadas pelos elementos:
# definição (def): atribuição do nome da função (referência à função)
# assinatura
# documentação (docstring): https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html

# parametros: não sabe o valor
#def nome_da_funcao(a, b, c):
def nome_da_funcao(a: int, b: int, c: int) -> int:

    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c quando o parametro a tiver o valor 10 vai acontecer x.

    :param a: Numero inteiro
    :type a: int
    :param b: Numero inteiro
    :type b: int
    :param c: Numero inteiro
    :type c: int
    :return: retorna o resultado de a + b + c
    :rtype: int
    """

    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c quando o parametro a tiver o valor 10 vai acontecer x.

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

valor = nome_da_funcao(1, 2, 3) # argumentos da função
print(valor)

###############################################################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    return a * 2, b * 2, c * 2

outro_valor = outra_funcao(1, 2, 3)
valor1, v2, v3 = outra_funcao(4, 5, 6)
print(outro_valor)
print(valor1, v2, v3)

primeiro, *resto = outra_funcao(100, 200, 300)
print(primeiro)
print(resto)

###############################################################

# Passagm de argumentos com desempacotamento
def soma(n1, n2):
    """Faz a soma de 2 números"""
    return n1 + n2

print(soma(10,20))
args = (30, 40)
print(soma(*args))

argsDict = {"n2":90, "n1":100}
#print(soma(argsDict["n1"],argsDict["n2"]))
print(soma(**argsDict))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 90},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13]
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))
