#!/usr/bin/env python3

import os
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

#BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)

# nossa instancia
log = logging.Logger("pati", log_level)
# level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)
"""
log.debug("Msg pro dev, qa, sysadmin")
log.info("Msg geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral: banco de dados sumiu")

"""

print("---")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("[ERRO] Deu erro %s", str(e))
    # stderr