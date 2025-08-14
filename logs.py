#!/usr/bin/env python3

import os
import logging
from logging import handlers

#BOILERPLATE
# TODO: Mover para módulo de utilizades
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("pati", log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, # 10**6
    backupCount=10
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)


"""
log.debug("Msg pro dev, qa, sysadmin")
log.info("Msg geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral: banco de dados sumiu")

"""

try:
    1/0
except ZeroDivisionError as e:
    log.error("[ERRO] Deu erro %s", str(e))
    # stderr