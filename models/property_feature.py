from init import db, ma
from marshmallow import fields

association_table = db.Table(
    "property_features",
    db.Column("property_id", db.ForeignKey("properties.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("features.id"), primary_key=True),
)

class Feature(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)


    properties = db.relationship("Property", secondary=association_table, back_populates="features")

class FeatureSchema(ma.Schema):
    class Meta:
        fields = ('id','name')
        ordered = True

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    garages = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   
    user = db.relationship("User", back_populates="properties")
    comments = db.relationship("Comment", back_populates="property", cascade="all, delete")

    features = db.relationship("Feature", secondary=association_table, back_populates="properties")

class PropertySchema(ma.Schema):
    class Meta:
        fields = ('id','address', 'state', 'postcode', 'bedrooms', 'bathrooms','garages')
        ordered = True