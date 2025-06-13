
from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    due_date = db.Column(db.String(80))

    def __init__(self, title, author_id, due_date=None):
        self.title = title
        self.author_id = author_id
        self.due_date = due_date

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id,
            'due_date': self.due_date
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()
