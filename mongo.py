from flask import Flask
from pymongo import MongoClient
from configparser import ConfigParser

app = Flask(__name__)
config = ConfigParser()
config.read('.config.cfg')
# Define global variables for the MongoDB connection and database
client = None
db = None
MONGO_URI = config.get("DATABASE","MONGO")

# Function to get the MongoDB connection
def get_mongo():
    global client
    print(MONGO_URI)
    if client is None:
        print("entering the myth....")
        client = MongoClient(MONGO_URI)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    return client

# Function to close the MongoDB connection
def close_mongo():
    global client
    if client is not None:
        client.close()

# Function to initialize the MongoDB database
def init_mongo():
    global db
    if db is None:
        client = get_mongo()
        db = client.aptData
        return db
