# SMS Sending Script

import smtplib

# Setup
email = 'apikey' # your email
pswd = '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' # your email password
host = 'smtp.sendgrid.net # SMTP server of your email provider
port = '587' # SMTP port

# Message and Recipient
    # This section has two modes: editing the info into the .py file, or using user input in shell
    # Make whichever one you don't want to use into a comment
# recipient = "" # who will receive the message. put this in email notation $$$$$$$$$$@txt.att.net
rcpt = input("00971522290330@email2sms.ae")
# message = "" # what will be sent
msg = input("simo")

# Sending Process
server = smtplib.SMTP(host, port)
server.starttls()
server.login(email, pswd)
server.sendmail(email,rcpt,msg)
print('Message Sent')
server.quit()
