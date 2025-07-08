#!/usr/bin/env python3

import logging

# nossa instancia
log = logging.Logger("pati", logging.DEBUG)
# level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)

log.debug("Msg pro dev, qa, sysadmin")
log.info("Msg geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral: banco de dados sumiu")

print("---")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("[ERRO] Deu erro %s", str(e))
    # stderr