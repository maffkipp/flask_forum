from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=50)

    def __repr__(self):
        return 'Comment: {}'.format(self.content)


class Post(Document):
    title = StringField(required=True)
    content = StringField()
    comments = ListField(EmbeddedDocumentField(Comment))
    name = StringField(max_length=50)

    def __repr__(self):
        return 'Post: {}'.format(self.content)
