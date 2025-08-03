

def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)
    print(kwargs)
    print(f"timeout: {timeout}")

funcao(
    "Pati",
    1,
    True,
    timeout=90,
    nome="Joana",
    cidade="Viana",
    data="hoje",
    banana=1
)

def titulo(nome):
    print(nome.title())

titulo("pati")