from flask import Flask
from flask_restful import Api
from db import db
from resources.book import BookList, BookResource
from resources.author import AuthorList, AuthorResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(BookList, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')
api.add_resource(AuthorList, '/authors')
api.add_resource(AuthorResource, '/authors/<int:author_id>')

if __name__ == '__main__':
    app.run(debug=True)
