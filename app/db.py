from pymongo import MongoClient
import os
import certifi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("DATABASE_URL", "mongodb+srv://...")

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client.loyaltea
offers_collection = db.offers
