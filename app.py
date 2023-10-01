from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
from flask import jsonify, request, Flask
import certifi
import json

# Create a new client and connect to the server
uri = "mongodb+srv://michaelnguyen:XAgiAkTP81ZzJ1bT@cluster0.aeeijua.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Select the database and collection
database_name = 'aptData'
# collection_name = 'aptData'
# db = client[database_name]
# collection = db[collection_name]
apt_data_collection = client[database_name]['aptData']
aggregated_data_collection = client[database_name]['aggregatedData']

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/getapts/', methods=['GET'])
def get_apts():
    unique_apts = apt_data_collection.distinct('Apt')
    return unique_apts


@app.route('/getyears/', methods=['GET'])
def get_years():
    unique_years = apt_data_collection.distinct('Year')
    return unique_years


@app.route('/submitform/', methods=['POST'])
def submit_form():
    data = request.data.decode('utf-8')  # Assuming the data sent is a JSON string
    data_dict = json.loads(data)
    
    # Ensure the entry has all necessary fields
    required_fields = {
        'Amenities', 'Apt', 'DoubleOcc', 'FiveStartRating',
        'NumBathrooms', 'NumBedrooms', 'Rent', 'Year', 'YearBuilt'
    }

    if not required_fields.issubset(data_dict.keys()):
        missing_fields = required_fields - data_dict.keys()
        return jsonify(error=f"Missing required fields: {', '.join(missing_fields)}"), 400
    
    # Insert the new survey entry into the aptData collection
    # Assuming you have already set up a connection to your MongoDB collection:
    aggregated_data_collection.insert_one(data_dict)

    return jsonify(success=True), 200


@app.route('/getapt/<apt_name>', methods=['GET'])
def get_apt_details(apt_name):
    print(apt_name)
    try:
        data = list(apt_data_collection.find({'Apt': apt_name}))
        return jsonify(data), 200
    except Exception as e:
        print(e)
        return jsonify({'success': False}), 401





