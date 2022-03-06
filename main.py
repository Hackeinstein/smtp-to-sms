import smtplib,ssl
import json

#lfuaytabwtlqxzka


print("""
|||||||  |||   ||   |||   ||||||| 
|||  ||| |||  ||||  |||   |||  |||  
|||  |||  ||| |||| |||    |||  |||  
|||  |||   ||||||||||     |||  |||  
|||||||     |||  ||||     ||||||| 
""")
print("WELCOME TO DARKWEBDEITY SMTP TO SMS TOOL")
print("")
print("This too is used to send messages to sms using smtp")
print("It uses the gateway system provide my sim carrier")
print("plese convert your number leads before use")
print("")
print("")

#code to collect smtp details

smtp_server = input("Enter Smtp server: ")
port = int(input("Enter Smtp port: "))
smtp_user= input("Enter Smtp user {sometimes same as sender email}: ")
sender_email =  input("Enter Sender email: ")
password = input("Type smtp password: ")

print("")
print("")

bank=input("Name of bank: ")
text_message=input("THe message to send dont add link: ")
link=input("Link to scama: ")

#code to collect list file

print("")
print("")

print("Now enter leads file")
filename=input("Enter file name: ")
print("")
print("")
file = open(filename, 'r')
lines = file.readlines()
for index,line in enumerate(lines):
    receiver_email=("{}".format( line.strip()))
    
    message = f"""\
    Subject: {bank}

    {text_message} {link}."""

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port) 
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email,message)
        print (receiver_email + " -- Sent")
    except Exception as ex:
        print (receiver_email+ " -- Not Sent",ex)

print("")
input("DONE")


    



