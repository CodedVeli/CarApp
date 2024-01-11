from app import db

class Car(db.Model):
    __tablename__ = 'cars'  
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64), index=True, unique=True)
    model = db.Column(db.String(64), index=True, unique=True)
    year = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id') , nullable=False )
    user = db.relationship('User')


    def serialize(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'user_details': self.user.serialize() if self.user else None
        }