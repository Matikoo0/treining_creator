import pymongo
from lib import getConfig

config=getConfig()
MONGOURL=config['MONGO']['URL']

db=pymongo.MongoClient(MONGOURL)


def add_workout(data:str):
    mydb=db["data"]
    work=mydb["workouts"]

    return work.insert_one(data)