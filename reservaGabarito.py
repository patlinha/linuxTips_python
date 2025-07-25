import sys
import logging

ocupados = {}
try:
    for line in open("reservas2.txt"):
        nome_quarto, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome_quarto,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas2.txt nao existe")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos2.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos2.txt nao existe")
    sys.exit(1)

if len(ocupados) == len(quartos):
    print("-" * 40)
    print("Hotel Lotado")
    print("-" * 40)
    sys.exit(1)


print("Reserva Hotel Pythonico")
print("-" * 40)
print("Lista de quartos:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "⛔" if not dados["disponivel"] else "👍🏾"
    #disponivel = dados["disponivel"] and "👍🏾" or "⛔"
    # TODO: Substituir casa deciaml por vírgula
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")
print("-" * 40)

nome = input("Nome do cliente: ").strip()
try: 
    num_quarto = int(input("Numero do quarto: ").strip())
    if not quartos[num_quarto]['disponivel']:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Numero inválido")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe")
    sys.exit(1)

try: 
    dias = int(input("Numero de dias: ").strip())
except ValueError:
    logging.error("Numero inválido")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

with open("reservas2.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n") 
    #file_.write(",".join[nome,str(num_quarto),str(dias)])

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R$ {total:.2f}")