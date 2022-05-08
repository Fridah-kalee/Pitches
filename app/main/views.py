from flask import render_template
from . import main
from ..models import Pitch


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting reviews by category
    interview_pitches = Pitch.get_pitches('interview')
    product_pitches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')

   
    
    
    title='Welcome to pitches website'

    return render_template('index.html',title=title,interview=interview_pitches,product=product_pitches,promotion=promotion_pitches)

@main.route('/pitches/product_pitches')
def product_pitches():

    pitches = Pitch.get_pitches('product')

    return render_template("product_pitches.html", pitches = pitches)

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interview')

    return render_template("interview_pitches.html", pitches = pitches)

@main.route('/pitches/promotion_pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches('promotion')

    return render_template("promotion_pitches.html", pitches = pitches)            

