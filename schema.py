#import all modules
import random
import os
import ssl
import certifi
from email import message
import time
from datetime import datetime
from smtplib import *
from threading import Thread
# requirement modules
from colorama import Fore, Back, Style, init
import numpy as np


#set super variaables
CONTEXT = ssl.create_default_context(cafile=certifi.where())
print("WELCOME TO SMTP TO SMS TOOL")
print("")
print("This too is used to send messages to sms using smtp")
print("It uses the gateway system provide my sim carrier")
print("plese convert your number leads before use")
print("")
print("")
init()

#set functions and import lists
#company list
with open("./modules/contents/company.txt","r")as company_file:
    company_list=company_file.readlines()
    company_list=[company.strip("\n") for company in company_list]

#list of charge vocubalaries
with open("./modules/contents/words.txt","r")as words_file:
    word_list=words_file.readlines()
    word_list=[word.strip("\n") for word in word_list]

#get list of links
with open("./modules/contents/link.txt","r")as links_file:
    link_list=links_file.readlines()
    link_list=[link.strip("\n") for link in link_list]


# functions
#generate random amounts
def random_amount(start:float, end:float) -> float:
    return random.randint(start,end)

# random company 
def random_company(company_list:list)->str:
    lenght=len(company_list)-1
    return company_list[random.randint(0,lenght)]

# random charge vocubalary
def random_word(word_list:list)->str:
    lenght=len(word_list)-1
    return word_list[random.randint(0,lenght)]

# random link
def random_link(word_list:list)->str:
    lenght=len(word_list)-1
    return word_list[random.randint(0,lenght)]

#merge text
def randomize(text:str, start:float, end:float)->str:
    #replace [company], ['word'], ['amount'], ['link'] keywords
    global company_list, word_list, link_list
    text = text.replace("[company]",random_company(company_list))
    text = text.replace("[word]",random_word(word_list))
    text = text.replace("[link]",random_link(link_list))
    text = text.replace("[amount]",str(random_amount(start,end)))
    return text
# send email
def send_message(smtp: list, _from: str, to: str, subject: str, content: str) -> str:
    global CONTEXT
    try:
        server = SMTP(host=smtp[0], port=int(smtp[1]))
        server.ehlo()
        server.starttls(context=CONTEXT)
        server.ehlo()
        server.login(user=smtp[2], password=smtp[3])
        msg = message.Message()
        msg.add_header('from', _from)
        msg.add_header('to', to)
        msg.add_header('subject', subject)
        msg.set_payload(content)
        server.send_message(msg, from_addr=_from, to_addrs=[to])
        return Fore.GREEN + f"message sent to {to}"
    except Exception as ex:
        # log error message
        with open("log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - {ex}\n")

        return Fore.RED+f"message not sent to {to}"

# collect config properties
multi_smtp=input(Fore.CYAN + "USE MULTIPLE SMTP [Y/N]: ").lower()
print("")
send_per_hour=int(input(Fore.CYAN + "ENABLE SEND PER HOUR LIMIT [ENTER AMOUNT TO ENABLE / 0 TO DISABLE]: "))
print("")
# get create a super function for sending and run

# since it uses default locations for smtps and other files you can process single smtp
if multi_smtp=="y":
    _from=input(Fore.CYAN + "SERVICE NAME / FROM NAME: ")
    print("")
    subject=input(Fore.CYAN + "ATTENTION CALL / SUBJECT: ")
    print("")
    content=input(Fore.CYAN + "ENTER YOUR CONTENT/BODY: ")
    print("")
    file_name=input(Fore.CYAN + "LEADS FILE LOCATION: ")
    print("")
    start_amount=float(input(Fore.CYAN + "START $ AMOUNT FOR RANDOMIZE [ENTER ZERO TO DISABLE]: "))
    print("")
    stop_amount=float(input(Fore.CYAN + "STOP $ AMOUNT FOR RANDOMIZE [ENTER ZERO TO DISABLE]: "))
    print("")

    

    #split smtp
    with open("./modules/contents/smtp.txt", "r") as file:
        smtp_list = file.readlines()
        # strip \n
        smtp_list = [item.strip("\n") for item in smtp_list]
        # split into indvidual smtp components
        smtp_list = [smtp.split("|") for smtp in smtp_list]

    index=len(smtp_list)
    #spilt leads
    with open(file_name,"r") as leads_file:
        leads=leads_file.readlines()
        leads=[lead.strip("\n") for lead in leads]
        leads=np.array_split(leads,index)
   
    # sending instructions
    def run_send(smtp: list, _from:str, subject:str, content:str, leads:list, start:float, stop:float):
        if send_per_hour > 0:
            count=0
            slow=(3600/send_per_hour)-2
        else:
                slow=0


        for lead in leads:
            print(send_message(smtp=smtp, _from=_from, to=lead, subject=subject, content=randomize(content,start,stop)))
            time.sleep(slow)
            if slow != 0:
                if count < send_per_hour:
                    count=+1
                elif count >= send_per_hour:
                    break
        

    #threads config
    threads=[]   
    for i in range(index):
        print(Fore.YELLOW + f"STARTING MAILER CHANNEL {i}")
        threads.append(Thread(target = run_send, args=(smtp_list[i], _from, subject, content, leads[i], start_amount, stop_amount, )))
    print(" ")
    print(" ")
    # start threads
    for thread in threads:
        thread.start()
    # join threads
    for thread in threads:
        thread.join
    input(Fore.CYAN+"DONE....")  

   
else:
    _from=input(Fore.CYAN + "SERVICE NAME / FROM NAME: ")
    print("")
    subject=input(Fore.CYAN + "ATTENTION CALL / SUBJECT: ")
    print("")
    content=input(Fore.CYAN + "ENTER YOUR CONTENT/BODY: ")
    print("")
    file_name=input(Fore.CYAN + "LEADS FILE LOCATION: ")
    print("")
    start_amount=float(input(Fore.CYAN + "START $ AMOUNT FOR RANDOMIZE [ENTER ZERO TO DISABLE]: "))
    print("")
    stop_amount=float(input(Fore.CYAN + "STOP $ AMOUNT FOR RANDOMIZE [ENTER ZERO TO DISABLE]: "))
    print("")

    #load leads and send files
    with open(file_name,"r") as leads_file:
        leads=leads_file.readlines()
        leads=[lead.strip("\n") for lead in leads]
    
    #load smtp file
    with open("./modules/contents/smtp.txt", "r") as smtp_file:
        smtp_list = smtp_file.readlines()
        # strip \n
        smtp_list = [item.strip("\n") for item in smtp_list]
        # split into indvidual smtp components
        smtp_list = [smtp.split("|") for smtp in smtp_list]
        if send_per_hour > 0:
            count=0
            slow=(3600/send_per_hour)-2
        else:
            slow=0


    for lead in leads:
        print(send_message(smtp=smtp_list[0], _from=_from, to=lead, subject=subject, content=randomize(content,start_amount,stop_amount)))
        time.sleep(slow)
        if slow != 0:
            if count < send_per_hour:
                count=+1
            elif count >= send_per_hour:
                break
    input(Fore.CYAN+"DONE....")










