import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    smtp_server = "smtp.gmail.com"
    port = 465  # SSL port

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")

def main():
    print("Otomatik E-posta Gönderici / Automatic Email Sender")
    sender_email = input("Gönderen E-posta Adresi (Gmail): ")
    sender_password = input("Gönderen E-posta Parolası: ")
    receiver_email = input("Alıcı E-posta Adresi: ")
    subject = input("Konu: ")
    body = input("Mesaj: ")

    send_email(sender_email, sender_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()
