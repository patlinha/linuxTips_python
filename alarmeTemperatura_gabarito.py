import logging

log = logging.Logger("alerta")

# TODO: Mover para módulo de utilidades

info = {"temperatura": None, "umidade": None}

def is_completly_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completly filled."""
    info_size = len(dict_of_inputs)
    filled_size = len([value for value in dict_of_inputs.values() if value is not None])
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input"""
    for key in dict_of_info.keys():
        if info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break


while not is_completly_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values()

if temp > 45:
    print("ALERTA!! Perigo calor extremo")
elif temp > 30 and temp*3 >= umidade:
    print("ALERTA!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("FRIO")
elif temp < 0:
    print("ALERTA!! Frio extremo")