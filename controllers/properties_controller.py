from flask import Blueprint, request
from init import db
from models.property_feature import Property, PropertySchema, Feature, FeatureSchema
from models.comment import Comment, CommentSchema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.auth_controller import authorize



properties_bp = Blueprint('properties', __name__, url_prefix='/properties')


@properties_bp.route('/', methods=['GET'])
def get_all_properties():
    stmt = db.select(Property) # using Select to create a new Property selection object
    properties = db.session.scalars(stmt) # Use session.scalars to call a new select object
    return PropertySchema(many=True).dump(properties) # Serialize Property and return them in JSON format
    


@properties_bp.route('/<int:property_id>/', methods=['GET'])
def get_one_property(property_id):
    stmt = db.select(Property).filter_by(id=property_id) # using Select to create a new Property selection object Filter condition set to id = property_id 
    property = db.session.scalar(stmt) # Use session.scalar to call a new select object
    if property:
        return PropertySchema().dump(property) #  Serialize Property and return them in JSON format
    else:
        return {'error': f'property not found with id {property_id}'}, 404  


@properties_bp.route('/', methods=['POST'])
@jwt_required()
def create_property():
    data = PropertySchema().load(request.json) # Deserialize JSON file Property into python object
    property = Property(
        address = data['address'],
        state = data['state'],
        postcode = data['postcode'],
        bedrooms = data['bedrooms'],
        bathrooms = data['bathrooms'],
        garages = data['garages'],
        user_id = get_jwt_identity()
    )
    db.session.add(property)
    db.session.commit()
    return PropertySchema().dump(property), 201

@properties_bp.route('/<int:property_id>/', methods=['DELETE'])
@jwt_required()
def delete_one_property(property_id):
    authorize()
    stmt = db.select(Property).filter_by(id=property_id) # using Select to create a new Property selection object Filter condition set to id = property_id 
    property = db.session.scalar(stmt) # Use session.scalar to call a new select object
    if property:
        db.session.delete(property)
        db.session.commit()
        return {'message': f"property '{property_id}' deleted successfully"}
    else:
        return {'error': f'property not found with id {property_id}'}, 404  

@properties_bp.route('/<int:property_id>/', methods = ['PUT','PATCH'])
@jwt_required()
def update_one_property(id):
    stmt = db.select(Property).filter_by(id=id)# using Select to create a new Property selection object Filter condition set to id = id
    property = db.session.scalar(stmt)  # Use session.scalar to call a new select object
    if property:
        property.address = request.json.get('address')
        property.state = request.json.get('state')
        property.postcode = request.json.get('postcode')
        property.bedrooms = request.json.get('bedrooms')
        property.bathrooms = request.json.get('bathrooms')
        property.garages = request.json.get('garages')
        db.session.commit()
        return PropertySchema().dump(property)
    else:
        return {'error': f'property not found with id {id}'}, 404

@properties_bp.route('/<int:property_id>/features/', methods=['POST'])
@jwt_required()
def add_feature_to_property(property_id):
    feature_id = request.json.get('feature_id')
    stmt = db.select(Property).filter_by(id=property_id) # using Select to create a new Property selection object Filter condition set to id = property_id
    property = db.session.scalar(stmt)
    
    stmt = db.select(Feature).filter_by(id=feature_id) # using Select to create a new Feature selection object Filter condition set to id = feature_id
    feature = db.session.scalar(stmt)
    if feature:
        # feature = request.json.get('name')
        property.features.append(feature.name)
        db.session.commit()

    return FeatureSchema(many=True).dump(property.features), 201


@properties_bp.route('/<int:property_id>/features/', methods=['GET'])
def show_property_features(property_id):
    stmt = db.select(Property).filter_by(id=property_id) # using Select to create a new Property selection object Filter condition set to id = property_id
    property = db.session.scalar(stmt)
    if property:
        return FeatureSchema(many=True).dump(property.features)
    else:
        return {'error': f'property not found with id {property_id}'}, 404

@properties_bp.route('/<int:property_id>/comments/', methods=['POST'])
@jwt_required()
def create_comment(property_id):
    stmt = db.select(Property).filter_by(id=property_id) # using Select to create a new Property selection object Filter condition set to id = property_id
    property = db.session.scalar(stmt)

    if property:
        comment = Comment(
        message = request.json['message'],
        property_id = request.json['property_id'],
        date = date.today(),
        user_id = get_jwt_identity()
        )
        db.session.add(comment)
        db.session.commit()
        return CommentSchema().dump(comment), 201
    else:
        return {'error': f'comment not found with property {property_id}'}, 404

@properties_bp.route('/<int:property_id>/features/', methods=['DELETE'])
@jwt_required()
def delete_one_feature(property_id):
    authorize()
    stmt = db.select(Feature).filter_by(property_id=property_id) # using Select to create a new Feature selection object Filter condition set to property_id = property_id
    feature = db.session.scalar(stmt)
    if feature:
        db.session.delete(feature)
        db.session.commit()
        return {'message': f"comment '{property_id}' deleted successfully"}
    else:
        return {'error': f'comment not found with id {property_id}'}, 404



@properties_bp.route('/<int:property_id>/comments/', methods=['GET'])
def get_one_comments(property_id):
    stmt = db.select(Comment).filter_by(property_id=property_id)  # using Select to create a new Comment selection object Filter condition set to property_id = property_id
    comments=db.session.scalars(stmt)
    if comments:
        return CommentSchema(many=True).dump(comments)
    else:
        return {'error': f'comment not found with id {property_id}'}, 404

@properties_bp.route('/<int:property_id>/comments/', methods=['DELETE'])
@jwt_required()
def delete_one_comment(property_id):
    authorize()
    stmt = db.select(Comment).filter_by(property_id=property_id)  # using Select to create a new Comment selection object Filter condition set to property_id = property_id
    comment = db.session.scalar(stmt)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return {'message': f"comment '{property_id}' deleted successfully"}
    else:
        return {'error': f'comment not found with id {property_id}'}, 404 

