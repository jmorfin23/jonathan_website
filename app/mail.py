from flask_mail import Message
from app import app, mail
from flask import render_template

def sendThemMail(name, email, subject, message):
    msg = Message(
        subject='Confirmation Email',
        sender=('Jonathan Morfin', app.config['ADMINS'][0]),
        recipients=[email],
    )
    msg.html = render_template('/email.html', name=name, message=message)

    mail.send(msg)

def sendMeMail(name, email, subject, message):

    mymsg = Message(
        subject= name + ' has sent you a message from your website!',
        sender=('Me', app.config['ADMINS'][0]),
        recipients=[app.config['ADMINS'][0]],
    )

    mymsg.html = render_template('/emailToMe.html', name=name, email=email, subject=subject, message=message)

    mail.send(mymsg)
