# Regras de negócio:
'''   
Problema: 
    Ir a padaria e comprar pão: 
Premissa: 
    Padaria da Esquina abre fds: até 12h, semana até 19h, feriado (exceto Natal) não abre.

A padaria está aberta?
    Se é feriado e NÃO é natal: não
    Senão, Se é sábado OU domingo E antes do meio dia: sim
    Senão, se é dia de semana E antes das 19h: sim
    senão: não
Se padaria está aberta E:
    Se está chovendo: Pegar guarda-chuvas
    Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
    Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
Ir até a padaria:
    Se tem pao integral E baguete: Pedir 6 de cada
    Senão, se tem apenas pao integral OU baguete: Pedir 12
    Senão: Pedir 6 de qualquer pão
Senão
    Ficar em casa em comer bolachas
'''


# PSEUDO CODIGO

import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
if natal and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
#elif today in feriado:
#    padaria_aberta = False
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo:
        pegar("guarda-chuva")
        if frio is False:
            pegar("agua")
        else:
            pegar("blusa")
            pegar("botas")
    
    ir("padaria")
    if tem("pao int") and tem("baguete"):
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem("pao int") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pao")

else:
    ficar("casa")
    comer("bolacha")

