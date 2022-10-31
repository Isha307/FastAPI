from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi


Client = MongoClient("mongodb+srv://test:test@cluster0.ax9ugoz.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
conn  = Client.Customer
'''m = client.test
try:
	client.admin.command('ismaster')
except ConnectionFailure:
    print("Server not available")

db = cluster["test"]
conn = db["User"]
post = {"_id": 0,
	"name": "isha",
	"email": "test@gmail.com",
	"password": "test"}

conn.insert_one(post)'''
