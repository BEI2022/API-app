from flask import Blueprint
from init import db
from models.comment import Comment, CommentSchema





comments_bp = Blueprint('comments', __name__, url_prefix='/comments')



@comments_bp.route('/', methods=['GET'])
def get_all_comments():
    stmt = db.select(Comment)
    comment=db.session.scalars(stmt)
    return CommentSchema(many=True).dump(comment)

@comments_bp.route('/<int:property_id>/', methods=['GET'])
def get_one_comments(property_id):
    stmt = db.select(Comment).filter_by(property_id=property_id)
    comments=db.session.scalars(stmt)
    if comments:
        return CommentSchema(many=True).dump(comments)
    else:
        return {'error': f'comment not found with id {property_id}'}, 404  






