from flask_restful import Resource, reqparse
from models.author import AuthorModel

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)

class AuthorList(Resource):
    def get(self):
        return {'authors': [author.json() for author in AuthorModel.get_all()]}

    def post(self):
        data = parser.parse_args()
        author = AuthorModel(**data)
        author.save_to_db()
        return author.json(), 201

class AuthorResource(Resource):
    def get(self, author_id):
        author = AuthorModel.find_by_id(author_id)
        if author:
            return author.json()
        return {'message': 'Author not found'}, 404

    def put(self, author_id):
        data = parser.parse_args()
        author = AuthorModel.find_by_id(author_id)

        if author:
            author.name = data['name']
        else:
            author = AuthorModel(**data)

        author.save_to_db()
        return author.json()

    def delete(self, author_id):
        author = AuthorModel.find_by_id(author_id)
        if author:
            author.delete_from_db()
            return {'message': 'Author deleted'}
        return {'message': 'Author not found'}, 404
