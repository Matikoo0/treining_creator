import pymongo
from lib import getConfig

config=getConfig()
MONGOURL=config['MONGO']['URL']

db=pymongo.MongoClient(MONGOURL)
mydb=db["data"]
work=mydb["workouts"]

def add_workout(data:str):

    return work.insert_one(data)

def get_workout_by_id(id:int):
    myquery={"id":id}
    return work.find(myquery)