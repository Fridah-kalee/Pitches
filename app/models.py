from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


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