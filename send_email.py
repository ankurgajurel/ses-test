import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SES_IDENTITY")
recipient_email = "ankurgajurel02@gmail.com"


def send_email():
    try:
        ses_smtp_port = os.getenv("SES_PORT")
        ses_smtp_host = os.getenv("SES_HOST")
        ses_username = os.getenv("SES_USER")
        ses_password = os.getenv("SES_PASS")

        subject = "Test Email"
        body = "This is a test email sent using Amazon SES SMTP."
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(ses_smtp_host, ses_smtp_port) as server:
            server.starttls()
            server.login(ses_username, ses_password)
            
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your SES SMTP credentials.")
    except smtplib.SMTPConnectError:
        print("SMTP Connect Error: Unable to connect to the SES SMTP server.")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_email()
