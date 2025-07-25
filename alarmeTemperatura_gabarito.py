import logging

log = logging.Logger("alerta")

# TODO: Usar funções para ler input

info = {"temperatura": None, "umidade": None}

while True:
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break

    if all(info.values()):
        break

    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

temp, umidade = info.values()

if temp > 45:
    print("ALERTA!! Calor extremo")
elif temp*3 >= umidade:
    print("ALERTA!! Calor úmido")
elif temp < 0:
    print("ALERTA: frio extremo")
elif temp <= 10:
    print("FRIO")
elif temp <= 30:
    print("Normal")