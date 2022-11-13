from flask import Blueprint,request
from init import db
from models.property_feature import Feature, FeatureSchema
from flask_jwt_extended import jwt_required


feature_bp = Blueprint('property_feature', __name__, url_prefix='/features')

@feature_bp.route('/', methods=['GET'])
def get_all_feature():
    stmt = db.select(Feature)
    feature=db.session.scalars(stmt)
    return FeatureSchema(many=True).dump(feature)

@feature_bp.route('/<int:feature_id>', methods=['GET'])
def get_one_feature(feature_id):
    stmt = db.select(Feature).filter_by(id=feature_id)
    feature = db.session.scalar(stmt)
    if feature:
        return FeatureSchema().dump(feature)
    else:
        return {'error': f'feature not found with id {feature_id}'}, 404  

@feature_bp.route('/<int:id>', methods = ['PUT','PATCH'])
@jwt_required()
def update_one_feature(id):
    stmt = db.select(Feature).filter_by(id=id)
    feature = db.session.scalar(stmt)
    if feature:
        feature.name = request.json.get('name')
        db.session.commit()
        return FeatureSchema().dump(feature)
    else:
        return {'error': f'feature not found with id {id}'}, 404