from app import db
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<User: {self.email}>'

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password) -> bool:
        print(password)
        print(self.password_hash)
        return self.password_hash == password

    @property
    def full_name(self) -> str:
        return ' '.join(self.first_name, self.last_name)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    calories = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User: {self.id}>'
