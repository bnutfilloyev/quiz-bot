from pymongo import MongoClient
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import IP

client = MongoClient(IP)
storage = MemoryStorage()

database = client['Quizzer']
user_db = database['users']
quizzes_database = database['quizzes_database']
quizzes_owners = database['quizzes_owners']
