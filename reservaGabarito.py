import sys
import logging

ARQUIVO_RESERVAS = "reservas2.txt"
ARQUIVO_QUARTOS = "quartos2.txt"

# TODO: usar função csv para ler os arquivos
ocupados = {}
try:
    for line in open(ARQUIVO_RESERVAS):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo %s nao existe", ARQUIVO_RESERVAS)
    sys.exit(1)

quartos = {}
try:
    for line in open(ARQUIVO_QUARTOS):
        codigo, nome_quarto, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), # TODO: Usar Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos2.txt nao existe")
    sys.exit(1)

if len(ocupados) == len(quartos):
    print("-" * 45)
    print(f"{"Hotel Lotado":^45}")
    print("-" * 45)
    sys.exit(0)

print("-" * 45)
print(f"{"Reserva Hotel Pythonico":^45}")
print("-" * 45)
print("Código - Nome do Quarto  - Preço       Vazio?")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome_quarto"]
    preco = dados["preco"]
    disponivel = "⛔" if not dados["disponivel"] else "👍🏾"
    #disponivel = dados["disponivel"] and "👍🏾" or "⛔"
    # TODO: Substituir casa deciaml por vírgula
    print(f"{codigo:<6} -{nome_quarto:<16} - R$ {preco:<9.2f} {disponivel}")
print("-" * 45)

nome = input("Nome do cliente: ").strip()
try: 
    num_quarto = int(input("Numero do quarto: ").strip())
    if not quartos[num_quarto]['disponivel']:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(0)
except ValueError:
    logging.error("Numero inválido")
    sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe")
    sys.exit(0)

try: 
    dias = int(input("Numero de dias: ").strip())
except ValueError:
    logging.error("Numero inválido")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * dias

print(f"Olá {nome}, você escolheu o quarto {nome_quarto} e vai custar: R$ {total:.2f}")

if input("Confirma a reserva? (S/n)").strip().lower() in ("sim","s"):
    with open("reservas2.txt", "a") as file_:
        file_.write(f"{nome},{num_quarto},{dias}\n") 
        #file_.write(",".join[nome,str(num_quarto),str(dias)])