from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, authenticate_user, infoUsuario

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET']) 
def get_events(): 
    return "Hello from user"

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = register_user(data['username'], data['password'])
    if user:
        return jsonify({'message': 'User registered successfully!'}), 201
    return jsonify({'message': 'User already exists!'}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data['username'], data['password'])
    if user:
        return jsonify({'message': 'Login successful!'})
    return jsonify({'message': 'Invalid credentials'}), 401

@user_bp.route('/info/<username>', methods=['GET']) 
def user_info(username):
    user = infoUsuario(username)
    
    if user:
        return jsonify({
           "id":user.id,
            "username": user.username,
            "password": user.password
            }), 200
    else: 
        return jsonify({"messege":"User not found"}), 400