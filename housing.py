import os
from flask import Flask, request, jsonify
from mongo import init_mongo, MongoClient
import bson.json_util as json_util

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    try:
        # Getting database and corresponding collection
        # with app.app_context():
        db = init_mongo()
        print("done wit init")
        collection = db.aptData
        print("here")
        data = list(collection.find({}))
        # Send token back to client
        return json_util.dumps(data), 200

    except Exception as e:
        print(e)
        # Return error if authentication fails
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401


if __name__ == "__main__":
    app.run(debug=True)