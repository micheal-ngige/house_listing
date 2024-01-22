from app import db

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    housetype = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable= False)
    price = db.Column(db.Float)
    description= db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reviews = db.relationship('Review', backref='house', lazy=True)
