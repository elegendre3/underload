import os

from pymongo import MongoClient


username = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'username')
password = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'password')
db_name = os.getenv('MONGO_INITDB_DATABASE', 'underload')

client = MongoClient(MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password)))

db = client[db_name]

document = db['document']

post_data = {
    'title': 'My Document',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = document.insert_one(post_data)
print('One doc: {0}'.format(result.inserted_id))
