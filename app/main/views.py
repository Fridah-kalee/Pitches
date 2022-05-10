from flask import render_template,url_for,request,redirect,abort
from . import main
from ..models import Pitch,User
from .forms import PitchForm,UpdateProfile
from flask_login import login_required
from .. import db


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

@main.route('/pitch/new',methods =['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        new_pitch=Pitch(pitch_title=title,pitch_content=content,pitch_category=category)

        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title='New Pitch'
    return render_template('new_pitch.html',title=title,pitch_form=form)



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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)                    

