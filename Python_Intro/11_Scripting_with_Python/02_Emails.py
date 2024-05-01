import smtplib

from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Tyler Scotti'
email['to'] = 'tylerscotti@yahoo.com'
email['subject'] = 'Click here for free cookies!'

email.set_content('This is a test for a python script')

with smtplib.SMTP(host='smtp.mail.yahoo.com', port=587) as smtp:
    smtp.ehlo()     # Server hello
    smtp.starttls() # Encryption 
    smtp.login('username@username.com', 'password123') #Login
    smtp.send_message(email)

