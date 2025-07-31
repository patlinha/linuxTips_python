#!/usr/bin/env python3
"""
Exemplos de envio de email
"""

#import smtplib
import aiosmtpd
SERVER = "localhost"
PORT = 8025

FROM = "patylinha@yahoo.com.br"
TO = ["areiasteste@gmail.com","a.patricia@aluno.ifsp.edu.br"]
SUBJECT = "Meu e-mail via python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá, mundo!</b>
"""

#SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with aiosmtpd.SMTP(host=SERVER, port = PORT) as server:server.sendmail(FROM, TO, message.encode("utf-8"))