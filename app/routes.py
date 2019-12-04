from app import app
from flask import render_template, url_for, redirect, flash
from flask import request, jsonify
from app.mail import sendThemMail, sendMeMail

@app.route('/')
def index():
    return 'This is a test.'


@app.route('/api/email')
def email():
    name = request.headers.get('name')
    email = request.headers.get('email')
    subject = request.headers.get('subject')
    message = request.headers.get('message')

    if not name or not email or not subject or not message:
        return jsonify({ 'Error 001:': 'Invalid parameters'})

    print('***************')
    print('***************')
    print(name, email, subject, message)
    print('***************')
    print('***************')

    sendThemMail(name=name, email=email, subject=subject, message=message)
    
    sendMeMail(name=name, email=email, subject=subject, message=message)

    return jsonify({ 'Success': 'Message was sent, thank you.'})
