from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi


Client = MongoClient("mongodb+srv://test:test@cluster0.ax9ugoz.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
conn  = Client.Customer
