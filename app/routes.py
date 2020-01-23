from app import app
from flask import render_template, url_for, redirect, flash
from flask import request, jsonify
from app.mail import sendThemMail, sendMeMail

@app.route('/')
def index():
    return 'This is a my portfolio backend.'


@app.route('/api/email')
def email():

    try:
        name = request.headers.get('name')
        email = request.headers.get('email')
        subject = request.headers.get('subject')
        message = request.headers.get('message')

        if not name or not email or not subject or not message:
            return jsonify({ 'Error': 'Please fill out the entire form.'})

        sendThemMail(name=name, email=email, subject=subject, message=message)

        sendMeMail(name=name, email=email, subject=subject, message=message)

        return jsonify({ 'Success': 'Message was sent, thank you.'})

    except:
        return jsonify({ 'Error': 'There was an error sending your message. Please try again.'})
