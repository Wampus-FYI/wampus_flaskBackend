@app.route('/register', methods=['POST'])
def register():
    # Get user credentials from client-side request
    email = request.json['email']
    password = request.json['password']

    try:
        # Create new user in Firebase Auth
        user = auth.create_user(email=email, password=password)
        token = auth.create_custom_token(user.uid)

        # Send token back to client
        return jsonify({'success': True, 'token': token.decode()}), 200

    except:
        # Return error if user creation fails
        return jsonify({'success': False, 'error': 'Failed to create user'}), 400
