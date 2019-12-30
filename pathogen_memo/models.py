"""
Models User / Pathogen
Demo, two tables no fk
"""

from datetime import datetime, timedelta

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db 

"""
Model: User
Created BY: https://hackersandslackers.com/flask-login-user-authentication/
Modified BY: NajlaBioinfo
"""
class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'flasklogin_users'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    website = db.Column(db.String(60),
                        index=False,
                        unique=False,
                        nullable=True)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


"""
Model : Pathogen
Created BY: NajlaBioinfo
"""
class Pathogen(db.Model):
    __tablename__ = 'pathogens'

    id = db.Column(db.Integer, primary_key=True)
    organism = db.Column(db.String())
    taxonid = db.Column(db.String())
    rank = db.Column(db.String())
    aerobe = db.Column(db.String())
    gram = db.Column(db.String())
    habitat = db.Column(db.String())
    isolation = db.Column(db.String())    
    pathostate = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __init__(self, name, author, published):
        self.organism = organism
        self.taxonid = taxonid
        self.rank = rank
        self.aerobe = aerobe
        self.gram = gram
        self.habitat = habitat
        self.isolation = isolation
        self.pathostate = pathostate

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'organism': self.organism, 
            'taxonid': self.taxonid,
            'rank': self.rank,
            'aerobe':self.aerobe,
            'gram': self.gram, 
            'habitat': self.habitat,
            'isolation': self.isolation,
            'pathostate':self.pathostate                     
        }