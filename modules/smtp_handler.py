from smtplib import *
import ssl
import json
import certifi
from email import message


context = ssl.create_default_context(cafile=certifi.where())

try:
    server=SMTP(host="smtp.strato.de",port=587)
    server.ehlo()
    server.starttls(context = context)
    server.ehlo()
    server.login(user="info@ect-wortmeier.de", password="083279h1")
    msg = message.Message()
    msg.add_header('from', "GATECITY")
    msg.add_header('to', "darkwebdeity@gmail.com")
    msg.add_header('subject', "atl jacob")
    msg.set_payload("falling out of love with you")
    server.send_message(msg, from_addr="info@ect-wortmeier.de", to_addrs=["3057998394@txt.att.net"])
except Exception as ex:
    print(ex)


