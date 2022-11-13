from init import db, ma 
from marshmallow import fields



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)


    property = db.relationship('Property', back_populates='comments')
    user = db.relationship('User', back_populates='comments')




class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'message', 'date')
        ordered = True