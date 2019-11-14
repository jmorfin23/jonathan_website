from app import app
from flask import render_template, url_for, redirect, flash
from flask import request, jsonify 


@app.route('/')
def index():
    return 'This is a test.'


@app.route('/api/email')
def email():
    name = request.headers.get('name')
    email = request.headers.get('email')
    subject = request.headers.get('subject')
    message = request.headers.get('message')

    print('***************')
    print('***************')
    print(name, email, subject, message)
    print('***************')
    print('***************')
