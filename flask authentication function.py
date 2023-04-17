import os
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import auth
from firebase_admin import credential
from configparser import ConfigParser

app = Flask(__name__)
config = ConfigParser()
config.read('.config.cfg')

FLASK_API = config.get("DATABASE","FIREBASE")
firebase_admin.initialize_app(FLASK_API)

@app.route('/login', methods=['POST'])
def login():
    # Get user credentials from client-side request
    email = request.json['email']
    password = request.json['password']

    try:
        # Authenticate user with Firebase
        user = auth.get_user_by_email(email)
        token = auth.create_custom_token(user.uid)

        # Send token back to client
        return jsonify({'success': True, 'token': token.decode()}), 200

    except:
        # Return error if authentication fails
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
