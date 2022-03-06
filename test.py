# Import smtplib for the actual sending function
import smtplib,ssl

# Import the email modules we'll need
from email.message import EmailMessage


# Create a text/plain message
msg = EmailMessage()
msg.set_content("hello this is a test")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "test subject"
msg['From'] = "darkwebdeity@yahoo.com"
msg['To'] = "darkwebdeity@gmail.com"

context = ssl.create_default_context()

# Send the message via our own SMTP server.
try:
    s = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.starttls(context=context)
    s.login("darkwebdeity@yahoo.com","lfuaytabwtlqxzka")
    s.sendmail(msg)
    s.quit()
except Exception as ex:
    print (ex)

input()