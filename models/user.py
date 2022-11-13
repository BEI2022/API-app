from init import db, ma 
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_PRIORITIES = ('buyer', 'seller', 'user')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique = True)
    password = db.Column(db.String, nullable=False)
    type = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    properties = db.relationship('Property', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')


class UserSchema(ma.Schema):
    type = fields.String(required=True,validate=OneOf(VALID_PRIORITIES))
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'type', 'is_admin')
        ordered = True
