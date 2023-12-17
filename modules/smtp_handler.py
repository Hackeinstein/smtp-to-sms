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
    server.login(user="#", password="#")
    msg = message.Message()
    msg.add_header('from', "GATECITY")
    msg.add_header('to', "#")
    msg.add_header('subject', "atl jacob")
    msg.set_payload("falling out of love with you")
    server.send_message(msg, from_addr="info@ect-wortmeier.de", to_addrs=["#"])
except Exception as ex:
    print(ex)


