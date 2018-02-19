# from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField
from app import db
from flask_mongoengine.wtf import model_form

# Comment model, associated with specific posts


class Comment(db.EmbeddedDocument):
    content = db.StringField()
    name = db.StringField(max_length=50)

    def __repr__(self):
        return 'Comment: {}'.format(self.content)


# Post model, has a list of comments. only title is required
class Post(db.Document):
    title = db.StringField(required=True, max_length=200)
    content = db.StringField()
    comments = db.ListField(db.EmbeddedDocumentField(Comment))
    name = db.StringField(max_length=50)

    def __repr__(self):
        return 'Post: {}'.format(self.content)


# Generate WTForms for each model
PostForm = model_form(Post)
CommentForm = model_form(Comment)
