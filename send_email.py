import smtplib
import ssl
from email.message import EmailMessage


# NB! The less secure feature on the recievers email address needs to be turned on.
# otherwise the receiver can not receive the email via this code.


subject = "Email from Python"
body = "This is ta test email from Python!"
sender_email = input("Enter your email: ")
receiver_email = input("Enter the receivers email: ")
password = input("Enter a password: ")

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    <body>
</html>
"""

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success!")