from init import db, ma 
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)


class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'message', 'date')
        ordered = True