from app import app
from flask import render_template, url_for, redirect, flash


@app.route('/')
def index():
    return 'This is a test.'
