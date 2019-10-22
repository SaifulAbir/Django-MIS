import smtplib, ssl
from sknf import settings

def send_email(sender_email, password, receiver_email, message):
   # Create a secure SSL context
   context = ssl.create_default_context()
   # Try to log in to server and send email
   try:
       server = smtplib.SMTP(EMAIL_HOST, config.smtp_port)
       server.ehlo()  # Can be omitted
       server.starttls(context=context)  # Secure the connection
       server.login(sender_email, password)
       # TODO: Send email here
       server.sendmail(sender_email, receiver_email, message)
   except Exception as e:
       # Print any error messages to stdout
       print(e)
   finally:
       server.quit()