import random

from pymongo import MongoClient
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import IP

client = MongoClient(IP)
storage = MemoryStorage()

database = client['Quizzer']
user_db = database['users']
quizzes_database = database['quizes_database']

if __name__ == "__main__":
    for i in quizzes_database.find():
        print(i['quiz_id'])

