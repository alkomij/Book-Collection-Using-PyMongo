from flask import Blueprint, request, jsonify
from models.user import User  # Adjust import path as necessary
from mongoengine.errors import NotUniqueError, ValidationError, DoesNotExist

user_routes = Blueprint('user_routes', __name__)

# Route to create a new user
@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        user = User(**user_data).save()
        return jsonify(user), 201
    except (NotUniqueError, ValidationError) as e:
        return jsonify({'error': str(e)}), 400

# Route to get all users
@user_routes.route('/', methods=['GET'])
def get_all_users():
    users = User.objects()
    return jsonify(users), 200

# Route to get a single user by id
@user_routes.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        return jsonify(user), 200
    except DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

# Route to update a user by id
@user_routes.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.json
        user = User.objects.get(id=user_id)
        user.update(**user_data)
        return jsonify(user.reload()), 200
    except (DoesNotExist, ValidationError) as e:
        return jsonify({'error': str(e)}), 400

# Route to delete a user by id
@user_routes.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return jsonify({'message': 'User deleted successfully'}), 200
    except DoesNotExist:
        return jsonify({'error': 'User not found'}), 404
