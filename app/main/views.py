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

