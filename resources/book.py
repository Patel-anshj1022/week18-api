from flask_restful import Resource, reqparse
from models.book import BookModel

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('author_id', type=int, required=True)
parser.add_argument('due_date', required=False)

class BookList(Resource):
    def get(self):
        return {'books': [book.json() for book in BookModel.get_all()]}

    def post(self):
        data = parser.parse_args()
        book = BookModel(**data)
        book.save_to_db()
        return book.json(), 201

class BookResource(Resource):
    def get(self, book_id):
        book = BookModel.find_by_id(book_id)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    def put(self, book_id):
        data = parser.parse_args()
        book = BookModel.find_by_id(book_id)

        if book:
            book.title = data['title']
            book.author_id = data['author_id']
            book.due_date = data['due_date']
        else:
            book = BookModel(**data)

        book.save_to_db()
        return book.json()

    def delete(self, book_id):
        book = BookModel.find_by_id(book_id)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted'}
        return {'message': 'Book not found'}, 404
