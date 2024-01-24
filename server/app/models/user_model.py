from app import db
from sqlalchemy.orm import validates
from flask import flash



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            flash('Username cannot be empty', 'error')
            raise ValueError('Username cannot be empty')
        if len(username) < 5:
            flash('Username must be at least 5 characters', 'error')
            raise ValueError('Username must be at least 5 characters')
        # Add more username validations as needed
        return username

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            flash('Password cannot be empty', 'error')
            raise ValueError('Password cannot be empty')
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            raise ValueError('Password must be at least 8 characters')
        # Add more password validations as needed
        return password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }