from pprint import pprint

import pymongo
from pymongo import MongoClient
from bson import ObjectId

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'posts_new'
MONGO_COLLECTION = 'news'
URI = 'mongodb://localhost:27017'

with MongoClient(URI) as client:
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    # db.drop_collection(MONGO_COLLECTION)

    doc = {
        "title": "Biden wins elections",
        "rating": 100.99,
        "likes": 12000
    }

    #collection.insert_one(doc)

    oid = '626195c756e0775a7b6e8b60'
    doc_for_exception = {
        "_id": ObjectId(oid),
        'title': 'murder in palace',
        'rating': 24.9
    }

    #collection.insert_one(doc_for_exception)

    # для нескольких документов collection.insert_many()

    # получаем курсор
    # found_docs = collection.find()

    found_docs = list(collection.find())

    def print_mongo_docs(cur):
        for i in cur:
            print(i)

    # print_mongo_docs(collection.find({'title': 'Biden wins elections'}))

    # print_mongo_docs(collection.find({'rating': {"$gt": -1}}))

    # print_mongo_docs(collection.find().sort("rating", pymongo.DESCENDING))

    # cur = collection.find()
    # cur.limit(3)
    #
    # cur.sort([
    #     ('rating', pymongo.ASCENDING),
    #     ('title', pymongo.DESCENDING)
    # ])
    #
    # print_mongo_docs(cur)

    # replace
    # collection.replace_one({
    #     "rating": 100.99
    #     },
    #     {
    #         "a": "Hurrah!"
    #     }
    # )
    # print_mongo_docs(collection.find({'a': 'Hurrah!'}))

    #update

    # collection.update_one(
    #     {
    #         'rating': 100.99
    #     },
    #     {
    #         '$set': {
    #             'rating': 50,
    #             'title': 'war'
    #         },
    #         '$unset': {
    #             'likes': None
    #         }
    #     }
    # )
    # print_mongo_docs(collection.find())

    # collection.update_many(
    #     {
    #         'rating': {'$gt': 99}
    #     },
    #     {
    #         '$inc': {
    #             'rating': 3
    #         }
    #     }
    # )
    # print_mongo_docs(collection.find({'rating': {'$gt': 99}}))

    # upsert создаст если не существует
    # collection.update_one({
    #     'rating': 64
    #     },
    #     {
    #         '$set': {
    #             'title': 'new star wars film'
    #         }
    #     },
    #     upsert=True
    # )
    # print_mongo_docs(collection.find({'rating': 64}))

    # collection.delete_many({'rating': 50})
    # print_mongo_docs(collection.find())
