from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False,unique=True)
    password=db.Column(db.String(120),nullable=False)
    trener_id = db.Column(db.Integer, db.ForeignKey('treiners.id'), nullable=True)

    def to_dict(self):
        return {'id':self.id,'name':self.name,
                'surname':self.surname,'email':self.email,
                'password':self.password,'trener_id':self.trener_id}

    def __repr__(self):
        return f'<User {self.name} {self.surname} , {self.email}>'


class Trener(db.Model):
    __tablename__ = 'treiners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False,unique=True)
    password=db.Column(db.String(120),nullable=False)
    podop = db.Column(db.String(240), nullable=True)

    def __repr__(self):
        return f'<Trener {self.name} {self.surname}>'

    def to_dict(self):
        return {'id': self.id, 'name': self.name,
                'surname': self.surname, 'email': self.email,
                'password':self.password, 'podop': self.podop}


class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    trener_id = db.Column(db.Integer, db.ForeignKey('treiners.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), nullable=False)
    zaang = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Exercise {self.name}>'

    def to_dict(self):
        return {'id': self.id, 'name': self.name,
                'url': self.url, 'trener': self.trener_id,
                'zaang': self.zaang}

