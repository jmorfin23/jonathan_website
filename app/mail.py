from flask_mail import Message
from app import app, mail


def sendMail(name, email, subject, message):

    print('test1')
    msg = Message(
        subject=subject,
        sender=email,
        recipients=['jmorfin776@gmail.com'],
        body=message
    )

    print('test2')
    mail.send(msg)

    print('test3')
