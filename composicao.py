"""Imprime apenas os nomes iniciados com a letra 1B'"""

names = [
    "Bruno", 
    "Joao", 
    "Bernardo", 
    "Barbara", 
    "Brian",
    ]


'''
def starts_with_b(text):
    #return text[0].lower() == "b"
    return text[0].startswith(("b","B"))
'''

# usando lambdas
# estilo funcional / declarativo
print(*list(filter(lambda text: text[0].lower() == "b",names)),sep="\n")

# estilo imperativo / procedural
"""
def starts_with_b(text):
    return text[0].lower() == "b"

filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
"""


"""
for name in names:
    if name.lower().startswith("b"):
        print(name)
"""