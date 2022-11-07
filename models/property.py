from init import db, ma
from marshmallow import fields


VALID_STATUSES = ('buyer', 'seller', 'user')

class Property(db.Model):
    __tablename__ = 'Property'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    barthrooms = db.Column(db.Integer, nullable=False)

class PropertySchema(ma.Schema):
    class Meta:
        fields = ('id','address', 'state', 'postcode', 'bedrooms', 'barthrooms','garages')