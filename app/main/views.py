from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='Welcome to pitches website'
    return render_template('index.html',title=title)