from app import db

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    usertype = db.Column(db.String(64))
    cars = db.relationship('Car', backref='owner', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'usertype': self.usertype,
        }