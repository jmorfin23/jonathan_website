from app import app
from flask import render_template, url_for, redirect, flash
from flask import request, jsonify
from app.mail import sendThemMail, sendMeMail
import json

@app.route('/')
def index():
    return 'This is a my portfolio backend.'


@app.route('/api/email')
def email():

    #retrieve data
    data = request.headers.get('data')

    #convert to a python dict
    mydata = json.loads(data)

    if not mydata['name'] or not mydata['email'] or not mydata['subject'] or not mydata['message']:
        return jsonify({ 'Error': 'Please fill out the entire form.'})

    sendThemMail(name=mydata['name'], email=mydata['email'], subject=mydata['subject'], message=mydata['message'])

    sendMeMail(name=mydata['name'], email=mydata['email'], subject=mydata['subject'], message=mydata['message'])

    return jsonify({ 'Success': 'Message was sent, thank you.'})
