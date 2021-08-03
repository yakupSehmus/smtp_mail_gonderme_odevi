import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

f = open("dosya.txt","r")

for i in range(5):
    mesaj = MIMEMultipart()

    mesaj["from"] = "mail"

    mesaj["to"] = f.readline()

    mesaj["subject"] = "başlık"

    yazi = "yazı"

    mesaj_gövdesi= MIMEText(yazi,"plain")

    mesaj.attach(mesaj_gövdesi)

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login("mail", "şifre")

        mail.sendmail(mesaj["from"], mesaj["to"], mesaj.as_string())

        print("mail gönderildi")

        mail.close()
    except:
        sys.stderr.write("bir sorun var")
        sys.stderr.flush()
f.close()