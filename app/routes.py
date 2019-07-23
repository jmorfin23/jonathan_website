from app import app
from flask import render_template, url_for, redirect, flash


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about-me')
def about_me():
    return render_template('about-me.html', title='About Me')


@app.route('/photos')
def photos():
    return render_template('photos.html', title='Photos')


@app.route('/follow Me')
def follow_me():
    return render_template('follow-me.html', title='Follow Me')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')
