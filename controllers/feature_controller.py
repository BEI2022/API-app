from flask import Blueprint,request
from init import db
from models.property_feature import Feature, FeatureSchema
from flask_jwt_extended import jwt_required


feature_bp = Blueprint('property_feature', __name__, url_prefix='/features')

@feature_bp.route('/', methods=['GET'])
def get_all_feature():
    stmt = db.select(Feature)  # using Select to create a new Feature selection object 
    feature=db.session.scalars(stmt) # Use session.scalars to call a new select object
    return FeatureSchema(many=True).dump(feature) # Serialize Feature and return them in JSON format

@feature_bp.route('/<int:feature_id>', methods=['GET'])
def get_one_feature(feature_id):
    stmt = db.select(Feature).filter_by(id=feature_id) # using Select to create a new Feature selection object Filter condition set to the input id = feature_id in the database
    feature = db.session.scalar(stmt) # Use session.scalar to call a new select object
    if feature:
        return FeatureSchema().dump(feature) # Serialize Feature and return them in JSON format
    else:
        return {'error': f'feature not found with id {feature_id}'}, 404  

@feature_bp.route('/<int:id>', methods = ['PUT','PATCH'])
@jwt_required()
def update_one_feature(id):
    stmt = db.select(Feature).filter_by(id=id) # using Select to create a new Feature selection object  Filter condition set to id = id 
    feature = db.session.scalar(stmt) # Use session.scalar to call a new select object
    if feature:
        feature.name = request.json.get('name')
        db.session.commit()
        return FeatureSchema().dump(feature)
    else:
        return {'error': f'feature not found with id {id}'}, 404