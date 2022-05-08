from . import db

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    # posted = db.Column(db.DateTime,default=datetime.utcnow)
    # user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # likes = db.Column(db.Integer)
    # dislikes = db.Column(db.Integer)

    # comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch