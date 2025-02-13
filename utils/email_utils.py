import smtplib
import ssl
from email.message import EmailMessage
import os

# Define email sender and receiver
email_sender = 'smaueltown@gmail.com'
email_password = os.environ['EMAIL_PASSWORD']
email_receiver = 'smaueltown@gmail.com'

def email_sam(subject: str, body: str):

    # Set the subject and body of the email
    subject = subject
    body = body

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f'sent email to {email_receiver}')