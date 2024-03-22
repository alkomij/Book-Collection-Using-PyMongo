from flask import Blueprint, request, jsonify
from models.book import Book  # Adjust the import path as necessary
from mongoengine.errors import NotUniqueError, ValidationError, DoesNotExist

book_routes = Blueprint('book_routes', __name__)

# Route to create a new book
@book_routes.route('/', methods=['POST'])
def add_book():
    try:
        book_data = request.json
        book = Book(**book_data).save()
        return jsonify(book), 201
    except (NotUniqueError, ValidationError) as e:
        return jsonify({'error': str(e)}), 400

# Route to get all books
@book_routes.route('/', methods=['GET'])
def get_books():
    books = Book.objects()
    return jsonify(books), 200

# Route to get a single book by id
@book_routes.route('/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        return jsonify(book), 200
    except DoesNotExist:
        return jsonify({'error': 'Book not found'}), 404

# Route to update a book by id
@book_routes.route('/<book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book_data = request.json
        book = Book.objects.get(id=book_id)
        book.update(**book_data)
        return jsonify(book.reload()), 200
    except (DoesNotExist, ValidationError) as e:
        return jsonify({'error': str(e)}), 400

# Route to delete a book by id
@book_routes.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return jsonify({'message': 'Book deleted successfully'}), 200
    except DoesNotExist:
        return jsonify({'error': 'Book not found'}), 404
