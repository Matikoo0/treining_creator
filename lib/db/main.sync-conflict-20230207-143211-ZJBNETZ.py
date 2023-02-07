import pymongo
from lib import getConfig

config=getConfig()
MONGOURL=config['MONGO']['URL']

myclient=pymongo.MongoClient(MONGOURL)

mydb=myclient["data"]
work=mydb["workouts"]