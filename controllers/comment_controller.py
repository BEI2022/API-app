from flask import Blueprint
from init import db
from models.comment import Comment, CommentSchema





comments_bp = Blueprint('comments', __name__, url_prefix='/comments')



@comments_bp.route('/', methods=['GET'])
def get_all_comments():
    stmt = db.select(Comment) # using Select to create a new Comment selection object 
    comment=db.session.scalars(stmt)  # Use session.scalars to call a new select object
    return CommentSchema(many=True).dump(comment) # Serialize Comment and return them in dict format


@comments_bp.route('/<int:property_id>/', methods=['GET'])
def get_one_comments(property_id):
    stmt = db.select(Comment).filter_by(property_id=property_id) # using Select to create a new Comment selection object Filter condition set to the input id = property_id in the database
    comments=db.session.scalars(stmt) # Use session.scalars to call a new select object
    if comments:
        return CommentSchema(many=True).dump(comments) # Serialize Comment and return them in JSON format
    else:
        return {'error': f'comment not found with id {property_id}'}, 404  






