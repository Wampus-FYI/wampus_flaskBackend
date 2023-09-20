from flask import jsonify, request, Flask
from pymongo import MongoClient
import timeit

# Database setup
MONGODB_SERVER = "mongodb+srv://michaelnguyen:VsjdSJlDxUiudmrK@cluster0.aeeijua.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_SERVER)

database_name = 'aptData'
collection_name = 'aptData'
db = client[database_name]
collection = db[collection_name]

app = Flask(__name__)

@app.route('/submitform/', methods=['POST'])
def submit_form():
    try:
        # Fetch the incoming JSON data
        data = request.get_json()

        # Insert into the MongoDB collection
        collection.insert_one(data)

        return jsonify({'success': True}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': 'Invalid data or database error'}), 400

if __name__ == "__main__":
    app.run(debug=True)
