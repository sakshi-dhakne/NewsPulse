import smtplib
from email.mime.text import MIMEText


def send_email(message):

    sender_email = "myemail@gmail.com"

    app_password = "my_password"

    receiver_email = "receivermail@gmail.com"

    msg = MIMEText(message)

    msg["Subject"] = "Daily News Digest"

    msg["From"] = sender_email

    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()

    print("Email sent successfully")