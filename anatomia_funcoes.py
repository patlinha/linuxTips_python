"""\
Este módulo serve apenas de anotação
"""


# as funções são formadas pelos elementos:
# definição (def): atribuição do nome da função (referência à função)
# assinatura
# documentação (docstring): https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html

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