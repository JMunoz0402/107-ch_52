import pymongo
import certifi

con_string = "mongodb+srv://jesusmunoz0402:Sandiego1!@fsdi-107.kz1ys.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("project1")