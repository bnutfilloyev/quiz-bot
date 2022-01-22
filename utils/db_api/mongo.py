from pymongo import MongoClient
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import IP

client = MongoClient(IP)
storage = MemoryStorage()

database = client['Quizzer']
user_db = database['users']
quizzes_database = database['quizes_database']
quizzes_owners = database['quizes_owners']

if __name__ == "__main__":
    print(quizzes_database.find_one_and_update())
    print(quizzes_owners)