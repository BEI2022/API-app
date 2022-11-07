from init import db, ma
from marshmallow import fields


class Feature(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)



class FeatureSchema(ma.Schema):
    class Meta:
        fields =('id', 'name')
