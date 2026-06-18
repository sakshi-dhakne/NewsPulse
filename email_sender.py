import smtplib
from email.mime.text import MIMEText

def send_email(sender,
               password,
               receiver,
               content):

    msg = MIMEText(content)

    msg["Subject"] = "Daily News Digest"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(sender, password)

        server.send_message(msg)

    print("Email sent")