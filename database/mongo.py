import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv("MongoDB_URI")


# Create a new client and connect to the server
server_api=ServerApi('1')
client = MongoClient(uri, server_api=server_api)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access the database
db = client['ecommerce']
