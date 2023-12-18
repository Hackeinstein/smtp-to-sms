from smtplib import *
import ssl
import json
import certifi
from email import message
from datetime import datetime

# import external ssl cert with certifi as python has issues detecting it
context = ssl.create_default_context(cafile=certifi.where())


# get list of smtp
with open("./contents/smtp.txt", "r") as file:
    smtp_list = file.readlines()
    # strip \n
    smtp_list = [item.strip("\n") for item in smtp_list]
    # split into indvidual smtp components
    smtp_list = [smtp.split("|") for smtp in smtp_list]
    print(smtp_list)


def send_message(smtp: list, _from: str, to: str, subject: str, content: str) -> str:
    try:
        server = SMTP(host=smtp[0], port=int(smtp[1]))
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(user=smtp[2], password=smtp[3])
        msg = message.Message()
        msg.add_header('from', _from)
        msg.add_header('to', to)
        msg.add_header('subject', subject)
        msg.set_payload(content)
        server.send_message(msg, from_addr=_from, to_addrs=[to])
        return f"message sent to {to}"
    except Exception as ex:
        # log error message
        with open("log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - {ex}\n")

        return f"message not sent to {to}"


# #check if its only one smtp and run it without threads
# if len(smtp_list) <=  1:

# else:
# # find a code to process all smtp as threads
#     pass
