import sys
import logging

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        #temperatura = float(input("Informe a temperatura: ").strip())
        info[key] = float(input(f"Informe a {key}: ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("ALERTA!! Calor extremo")
elif temperatura*3 >= umidade:
    print("ALERTA!! Calor úmido")
elif temperatura < 0:
    print("ALERTA: frio extremo")
elif temperatura <= 10:
    print("FRIO")
elif temperatura <= 30:
    print("Normal")
