from flask import Blueprint, request, jsonify
from models.transaction import Transaction  # Adjust import path as necessary
from mongoengine.errors import ValidationError, DoesNotExist

transaction_routes = Blueprint('transaction_routes', __name__)

# Route to create a new transaction
@transaction_routes.route('/', methods=['POST'])
def create_transaction():
    try:
        transaction_data = request.json
        transaction = Transaction(**transaction_data).save()
        return jsonify(transaction), 201
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400

# Route to get all transactions
@transaction_routes.route('/', methods=['GET'])
def get_all_transactions():
    transactions = Transaction.objects()
    return jsonify(transactions), 200

# Route to get all transactions for a specific user
@transaction_routes.route('/user/<user_id>', methods=['GET'])
def get_user_transactions(user_id):
    transactions = Transaction.objects(userId=user_id)
    return jsonify(transactions), 200

# Route to mark a transaction as returned
@transaction_routes.route('/<transaction_id>/return', methods=['PATCH'])
def mark_transaction_returned(transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.returned = True
        transaction.save()
        return jsonify(transaction), 200
    except DoesNotExist:
        return jsonify({'error': 'Transaction not found'}), 404

# Route to update a transaction by ID
@transaction_routes.route('/<transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    try:
        transaction_data = request.json
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.update(**transaction_data)
        return jsonify(transaction.reload()), 200
    except (DoesNotExist, ValidationError) as e:
        return jsonify({'error': str(e)}), 400

# Route to delete a transaction by ID
@transaction_routes.route('/<transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.delete()
        return jsonify({'message': 'Transaction deleted successfully'}), 200
    except DoesNotExist:
        return jsonify({'error': 'Transaction not found'}), 404
