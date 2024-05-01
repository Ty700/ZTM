# What if we wanted to customize the email??
# We can use a html email

# I can't send emails, I always get an error, idk. Supposed to be something about authentication

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # Essentially os.path

email = EmailMessage()

email['from'] = 'Tyler Scotti'
email['to'] = 'tylerscotti@yahoo.com'
email['subject'] = 'Click here for free cookies!'

html = Template(Path('./index.html').read_text()) 

email.set_content(html.substitute({'name': 'Tyler'}), 'html')

email.set_content('This is a test for a python script')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()     # Server hello
    smtp.starttls() # Encryption 
    smtp.login('username@username.com', 'password123') #Login
    smtp.send_message(email)

